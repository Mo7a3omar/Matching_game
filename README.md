# Matching_game
\documentclass{article}
\usepackage{hyperref}
\usepackage{listings}
\usepackage{color}
\usepackage{graphicx}

\title{Shape Matching Game}
\author{}
\date{}

\begin{document}

\maketitle

\section*{Description}

This is a fun and interactive shape matching game for kids using computer vision and hand tracking. The game allows children to drag and match shapes to their corresponding outlines using their fingers. It also features a "New Game" button to randomize the shapes and start a new game.

\section*{Features}

\begin{itemize}
    \item \textbf{Interactive Shape Matching}: Drag and drop shapes to match their corresponding outlines.
    \item \textbf{Real-time Hand Tracking}: Uses Mediapipe for real-time hand tracking and interaction.
    \item \textbf{Multiple Shape Dragging}: Allows dragging of multiple shapes simultaneously.
    \item \textbf{New Game Button}: Start a new game by randomizing the positions of the shapes.
\end{itemize}

\section*{Requirements}

\begin{itemize}
    \item Python 3.7 or higher
    \item OpenCV
    \item Mediapipe
    \item NumPy
\end{itemize}

\section*{Installation}

\begin{enumerate}
    \item Clone the repository:
    \begin{lstlisting}[language=bash]
    git clone https://github.com/yourusername/shape-matching-game.git
    cd shape-matching-game
    \end{lstlisting}

    \item Install the required dependencies:
    \begin{lstlisting}[language=bash]
    pip install opencv-python mediapipe numpy
    \end{lstlisting}
\end{enumerate}

\section*{Usage}

\begin{enumerate}
    \item Run the game script:
    \begin{lstlisting}[language=bash]
    python game.py
    \end{lstlisting}

    \item The game window will open, showing the shapes and their corresponding outlines.

    \item Use your index fingers to drag and drop the shapes to match their outlines.

    \item Click the "New Game" button in the top-right corner to randomize the positions of the shapes and start a new game.
\end{enumerate}

\section*{How It Works}

\begin{itemize}
    \item The game uses the webcam to capture real-time video.
    \item Mediapipe is used to detect and track hand landmarks.
    \item OpenCV is used to draw shapes and handle the drag-and-drop interaction.
    \item When a shape is close to its target position, it snaps into place and changes color.
\end{itemize}

\section*{Code Overview}

\begin{itemize}
    \item \textbf{game.py}: Main script containing the game logic, shape class, and hand tracking implementation.
\end{itemize}

\section*{Contributing}

Contributions are welcome! Please feel free to submit a pull request or open an issue to discuss any changes or improvements.

\section*{License}

This project is licensed under the MIT License - see the \href{LICENSE}{LICENSE} file for details.

\section*{Acknowledgements}

\begin{itemize}
    \item \href{https://github.com/google/mediapipe}{Mediapipe} for the hand tracking library.
    \item \href{https://opencv.org/}{OpenCV} for the computer vision library.
\end{itemize}

\end{document}
