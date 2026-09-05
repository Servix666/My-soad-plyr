import os
import sys
import time
import pygame

# --- ANSI COLOR CODES ---
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"

# --- LYRIC DATASET ---
# Format: (Timestamp_in_Seconds, Color, "Lyric Line")
# Structured around the song sections you provided: intro, riffs, verses, chorus, later cycle, ending.
LYRICS = [
    (0.00, WHITE, "..."),

    # 0:00-0:14 intro
    (0.00, RED, "..."),
    (6.00, CYAN, "..."),
    (12.00, YELLOW, "..."),

    # 0:14-0:28 main riff
    (29.00, RED, "Peter's pecker picked another"),
    (29.50, GREEN, "Pickle bearing pussy pepper"),
    (30.50, CYAN, "Peter's pecker picked another"),
    (32.00, YELLOW, "Pickle bearing pussy pepper, why"),

    # 0:28-0:35 verse 1
    (36.00, BLUE, "Meeting John at Dale's Jr."),
    (37.00, MAGENTA, "Winked an eye and point a finger"),
    (38.00, RED, "Meeting John at Dale's Jr., why"),

    # 0:36-0:42 verse 2
    (43.00, GREEN, "A former cop, undercover"),
    (44.00, CYAN, "Just got shot, now recovered"),
    (45.00, YELLOW, "A former cop, undercover"),
    (46.00, YELLOW, "Just got shot, now recovered"),

    # 0:43-0:49 verse 3
    (49.00, BLUE, "Fighting crime, with a partner"),
    (50.00, MAGENTA, "Lois Lane, Jimmy Carter"),
    (52.40, RED, "Fighting crime, with a partner"),
    (53.00, MAGENTA, "Lois Lane, Jimmy Carter"),

    # 0:57-1:03 chorus
    (57.00, BLUE, "I-E-A-I-A-I-O"),
    (61.00, MAGENTA, "I-E-A-I-A-I-O, why"),
    (63.00, RED, "As we light up the sky"),

    (72.00, RED, "Peter's pecker picked another"),
    (73.00, GREEN, "Pickle bearing pussy pepper"),
    (74.00, CYAN, "Peter's pecker picked another"),
    (75.00, YELLOW, "Pickle bearing pussy pepper, why"),

    # 1:04 onward main riff / second cycle
    (79.00, BLUE, "Meeting John at Dale's Jr."),
    (80.00, MAGENTA, "Winked an eye and point a finger"),
    (81.00, RED, "Meeting John at Dale's Jr."),
    (82.00, GREEN, "Winked an eye and point a finger, why"),
    (86.00, CYAN, "A former cop, undercover"),
    (87.00, YELLOW, "Just got shot, now recovered"),
    (88.00, BLUE, "A former cop, undercover"),
    (88.50, MAGENTA, "Just got shot, now recovered, why"),
    (93.00, RED, "Fighting crime, with a partner"),
    (94.00, GREEN, "Lois Lane, Jimmy Carter"),
    (95.00, CYAN, "Fighting crime, with a partner"),
    (95.50, YELLOW, "Lois Lane, Jimmy Carter"),

    # later chorus / bridge
    (101.00, BLUE, "I-E-A-I-A-I-O"),
    (103.50, MAGENTA, "I-E-A-I-A-I-O, why"),
    (110.00, RED, "As we light up the sky"),
    (115.00, GREEN, "I-E-A-I-A-I-O"),
    (119.00, CYAN, "I-E-A-I-A-I-O, why"),
    (125.00, YELLOW, "As we light up the sky"),
    (130.00, YELLOW, "....."),

    (144.00, BLUE, "Mine delusions acquainted"),
    (147.00, MAGENTA, "Bubbles erotica"),
    (148.00, RED, "Plutonium wedding rings"),
    (150.00, GREEN, "Icicles stretching"),
    (152.00, CYAN, "Bicycles, shoestrings"),
    (155.00, YELLOW, "One flag, flaggy but one"),
    (155.80, BLUE, "Painting the paintings of the alive"),

    (159.00, MAGENTA, "I-E-A-I-A-I-O"),
    (162.00, RED, "I-E-A-I-A-I-O, why"),
    (168.00, CYAN, "As we light up the sky"),
    (173.00, YELLOW, "I-E-A-I-A-I-O"),
    (177.00, BLUE, "I-E-A-I-A-I-O, why"),
    (183.00, GREEN, "As we light up the sky"),
]

AUDIO_FILE = "ieaiaio.mp3"
TOTAL_DURATION = 189.0  # Matches the ending cadence to the song structure


AUDIO_FILE = "ieaiaio.mp3"
TOTAL_DURATION = 189.0  # Extended total length for the remaining lyric sequence


def format_time(seconds):
    mins = int(seconds) // 60
    secs = int(seconds) % 60
    return f"{mins:02d}:{secs:02d}"


def draw_progress_bar(current, total, length=20):
    percent = min(1.0, current / total)
    filled = int(length * percent)
    bar = (
        "=" * filled + ">" + "-" * (length - filled - 1)
        if filled < length
        else "=" * length
    )
    return f"[{bar}]"


def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush()


def show_cursor():
    sys.stdout.write("\033[?25h")
    sys.stdout.flush()


def render_frame(header, lyric_display, timer_display):
    sys.stdout.write("\033[H")
    lines = [header, "", lyric_display, "", timer_display]
    for index, line in enumerate(lines, start=1):
        sys.stdout.write(f"\033[{index};1H\033[2K{line}\n")
    sys.stdout.flush()

def play_terminal_player():
    pygame.mixer.init()

    if os.path.exists(AUDIO_FILE):
        pygame.mixer.music.load(AUDIO_FILE)
        pygame.mixer.music.play()

    start_time = time.time()
    hide_cursor()

    try:
        while True:
            elapsed = time.time() - start_time
            if elapsed > TOTAL_DURATION:
                break

            # Find current active line
            active_line = ""
            active_color = WHITE
            for ts, color, line in LYRICS:
                if elapsed >= ts:
                    active_line = line
                    active_color = color

            # UI Strings matching the screenshot layout
            header = f"{MAGENTA}System of a Down{RESET} :: {CYAN}I-E-A-I-A-I-O{RESET} (Official Single) [ {GREEN}PLAYING{RESET} ]"
            lyric_display = (
                f"» {active_color}{active_line}{RESET}"
                if active_line
                else "» ..."
            )
            progress = draw_progress_bar(elapsed, TOTAL_DURATION)
            timer_display = f"{format_time(elapsed)} / {format_time(TOTAL_DURATION)} {progress}"

            render_frame(header, lyric_display, timer_display)
            time.sleep(0.1)

    except KeyboardInterrupt:
        pygame.mixer.music.stop()
        print("\nPlayback Stopped.")
    finally:
        show_cursor()


if __name__ == "__main__":
    play_terminal_player()