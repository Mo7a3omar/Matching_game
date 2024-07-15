import cv2
import mediapipe as mp
import numpy as np
import random

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# Initialize Mediapipe hand detector
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)
mp_draw = mp.solutions.drawing_utils

# Define shapes and their colors
shapes = ['circle', 'square', 'triangle', 'star']
colors = [(255, 0, 0), (0, 255, 0), (0, 255, 255), (255, 0, 255)]

# Define target positions for shapes
target_positions = [(200, 400), (400, 400), (600, 400), (800, 400)]

class Shape():
    def __init__(self, shape, initialPos, targetPos, color):
        self.shape = shape
        self.initialPos = initialPos
        self.posCenter = initialPos
        self.targetPos = targetPos
        self.color = color
        self.dragging = False
        self.snapped = False

    def draw(self, img):
        cx, cy = self.posCenter
        tx, ty = self.targetPos
        color = self.color if not self.snapped else (0, 255, 0)
        if self.shape == 'circle':
            cv2.circle(img, (cx, cy), 50, color, -1)
            if not self.snapped:
                cv2.circle(img, (tx, ty), 50, (255, 255, 255), 2)
        elif self.shape == 'square':
            cv2.rectangle(img, (cx - 50, cy - 50), (cx + 50, cy + 50), color, -1)
            if not self.snapped:
                cv2.rectangle(img, (tx - 50, ty - 50), (tx + 50, ty + 50), (255, 255, 255), 2)
        elif self.shape == 'triangle':
            pts = np.array([[cx, cy - 58], [cx - 50, cy + 29], [cx + 50, cy + 29]], np.int32)
            cv2.fillPoly(img, [pts], color)
            if not self.snapped:
                pts = np.array([[tx, ty - 58], [tx - 50, ty + 29], [tx + 50, ty + 29]], np.int32)
                cv2.polylines(img, [pts], True, (255, 255, 255), 2)
        elif self.shape == 'star':
            pts = np.array([[cx, cy - 58], [cx + 14, cy - 14], [cx + 58, cy], [cx + 14, cy + 14], [cx, cy + 58],
                            [cx - 14, cy + 14], [cx - 58, cy], [cx - 14, cy - 14]], np.int32)
            cv2.fillPoly(img, [pts], color)
            if not self.snapped:
                pts = np.array([[tx, ty - 58], [tx + 14, ty - 14], [tx + 58, ty], [tx + 14, ty + 14], [tx, ty + 58],
                                [tx - 14, ty + 14], [tx - 58, ty], [tx - 14, ty - 14]], np.int32)
                cv2.polylines(img, [pts], True, (255, 255, 255), 2)

    def update(self, cursor):
        if cursor is None or self.snapped:
            return
        
        cx, cy = self.posCenter
        tx, ty = self.targetPos

        # Calculate distance from cursor to shape center
        dist_to_center = np.linalg.norm(np.array(cursor) - np.array([cx, cy]))
        dist_to_target = np.linalg.norm(np.array(cursor) - np.array([tx, ty]))

        # If dragging and distance to target is less than snap threshold, snap it
        if self.dragging and dist_to_target < 50:
            self.snapped = True
            self.posCenter = self.targetPos
        elif self.dragging and dist_to_center > 100:
            self.dragging = False
        elif cx - 50 < cursor[0] < cx + 50 and cy - 50 < cursor[1] < cy + 50:
            # If the index finger tip is in the shape region, start dragging
            self.dragging = True

        # Update position if dragging
        if self.dragging:
            self.posCenter = cursor

# Initialize shapes
def initialize_shapes():
    shape_list = []
    random_initial_positions = random.sample(initial_positions, len(initial_positions))
    for i in range(4):
        shape_list.append(Shape(shapes[i], random_initial_positions[i], target_positions[i], colors[i]))
    return shape_list

initial_positions = [(150, 150), (400, 150), (650, 150), (900, 150)]
shape_list = initialize_shapes()

# Button to start new game
button_pos = (1080, 20)
button_size = (150, 50)

def draw_button(img):
    cv2.rectangle(img, button_pos, (button_pos[0] + button_size[0], button_pos[1] + button_size[1]), (0, 0, 255), -1)
    cv2.putText(img, "New Game", (button_pos[0] + 15, button_pos[1] + 35), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

def check_button_click(cursor):
    if cursor and button_pos[0] < cursor[0] < button_pos[0] + button_size[0] and button_pos[1] < cursor[1] < button_pos[1] + button_size[1]:
        return True
    return False

# Main loop
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    cursors = []
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            lmList = [(int(lm.x * img.shape[1]), int(lm.y * img.shape[0])) for lm in hand_landmarks.landmark]
            cursors.append(lmList[8])  # Get position of landmark 8 (index finger tip)

            # Draw landmarks
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Check button click
    if any(check_button_click(cursor) for cursor in cursors):
        shape_list = initialize_shapes()

    # Draw shapes
    for cursor in cursors:
        for shape in shape_list:
            shape.update(cursor)
    for shape in shape_list:
        shape.draw(img)

    # Add title
    cv2.putText(img, "Shape Matching Game", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Draw new game button
    draw_button(img)

    # Display output
    cv2.imshow("Shape Matching Game", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
