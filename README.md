# My-soad-plyr
Python Based Script to play songs (System Of A Down's I-E-A-I-A-I-O for this one)
# 🎵 I-E-A-I-A-I-O — Terminal Music Player

A simple **Python-based terminal music player** built manually in **VS Code** using **Pygame**.

This project is specifically designed to play **"I-E-A-I-A-I-O" by System of a Down** while displaying synchronized, color-coded lyrics directly in the terminal.

> ⚠️ **This is a single-song player created as a programming project. It is not intended to be a full-featured music player.**

---

## ✨ Features

* 🎵 Plays an audio file using **Pygame**
* 🖥️ Runs directly inside the **terminal**
* 🎨 Color-coded lyric display using **ANSI escape codes**
* ⏱️ Live playback timer
* 📊 Terminal progress bar
* 📝 Timestamp-based lyric synchronization
* ▶️ Automatically starts playback when the program runs
* ⌨️ `Ctrl + C` to stop playback
* 🧹 Dynamically updates the terminal instead of printing a new screen every frame

---

## 🛠️ Technologies Used

* **Python 3**
* **Pygame**
* **VS Code**
* **ANSI Escape Codes**
* Python standard libraries:

  * `os`
  * `sys`
  * `time`

---

## 📂 Project Structure

```text
I-E-A-I-A-I-O/
│
├── terminal_player.py
├── ieaiaio.mp3
├── README.md
```

> If you don't upload the MP3 to GitHub, the project can simply contain the Python source code and documentation. Users can provide their own legally obtained audio file locally.

---

## 🚀 How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check with:

```bash
python --version
```

### 2. Install Pygame

Open the VS Code terminal and run:

```bash
pip install pygame
```

### 3. Add the audio file

Download the Audio file online. Can't post here due to Copyright Issues. 
After downloading, rename it as "ieaiaio.mp3". 

This is the song's Youtube link : https://youtu.be/eudOwe3Rz-0?si=ZX9KMX0q3kDWiTum

Artist : System Of The Down

Place the required audio file in the same directory as `terminal_player.py`:

```text
I-E-A-I-A-I-O/
├── terminal_player.py
└── ieaiaio.mp3
```

### 4. Run the program

The terminal player will start automatically.

---

## 🖥️ Terminal Interface

The program displays information similar to:

```text
System of a Down :: I-E-A-I-A-I-O (Official Single) [ PLAYING ]

» [current lyric]

00:42 / 03:09 [========>-----------]
```

The interface continuously updates while the song is playing.

---

## ⚙️ How It Works

### 1. Audio Playback

Pygame's mixer module is used to initialize the audio system and play the song:

```python
pygame.mixer.init()
pygame.mixer.music.load(AUDIO_FILE)
pygame.mixer.music.play()
```

### 2. Timestamped Lyrics

Lyrics are stored in a Python list containing:

```text
(timestamp, color, lyric)
```

For example:

```python
(timestamp, color, "Lyric Line")
```

The program compares the current playback time with each timestamp and determines which line should currently be displayed.

### 3. ANSI Colors

ANSI escape codes are used to display lyrics in different terminal colors.

The project defines colors such as:

```python
RED
GREEN
YELLOW
BLUE
MAGENTA
CYAN
WHITE
```

This allows different lyric lines to appear in different colors.

### 4. Progress Bar

The program calculates the percentage of the song that has played and generates a terminal progress bar:

```text
[==========>---------]
```

### 5. Live Terminal Rendering

Instead of continuously printing new lines, the program uses ANSI cursor-control sequences to update the existing terminal interface.

This creates a simple animated terminal UI.

---

## 📚 What I Learned

This project helped me practice:

* Python functions
* Lists and tuples
* Conditional statements
* Loops
* Time tracking
* File existence checking
* Audio playback with Pygame
* ANSI terminal control
* String formatting
* Terminal-based UI design
* Handling `KeyboardInterrupt`
* Structuring a small Python project

---

## 🔮 Possible Future Improvements

Some features that could be added later:

* ⏯️ Pause / resume
* 🔊 Volume control
* ⏩ Seek forward/backward
* 🎵 Support for multiple songs
* 📃 Playlist support
* 🎨 More advanced terminal UI
* 🎚️ Volume indicator
* ⚙️ Command-line arguments
* 🎤 Improved lyric synchronization

---

## 👨‍💻 Author

**Servix666**
**(https://github.com/Servix666)**

Built manually from scratch using **Python and VS Code**.

---

## 📜 Disclaimer

This project was created for **educational and programming purposes**.

The song, audio recording, and lyrics are the property of their respective copyright holders. This repository should not be used to redistribute copyrighted material without appropriate permission.
