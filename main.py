import sounddevice as sd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

# General settings
SAMPLE_FREQ = 44100  # sample frequency in Hz
WINDOW_SIZE = 44100  # window size of the DFT in samples
WINDOW_STEP = 21050  # step size of window
windowSamples = [0 for _ in range(WINDOW_SIZE)]

# This function finds the closest note for a given pitch
# Returns: note (e.g. A4, G#3, ..), pitch of the tone
CONCERT_PITCH = 440
ALL_NOTES = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]


def find_closest_note(pitch):
    i = int(np.round(np.log2(pitch / CONCERT_PITCH) * 12))
    closest_note = ALL_NOTES[i % 12] + str(4 + (i + 9) // 12)
    closest_pitch = CONCERT_PITCH * 2 ** (i / 12)
    return closest_note, closest_pitch


def stop_callback():
    global is_stopped
    if is_stopped:
        is_stopped = False
    else:
        is_stopped = True


def show_popup(message):
    label.config(text=message)


# The sounddevice callback function
def callback(indata, frames, time, status):
    global windowSamples, is_stopped
    if status:
        print(status)
    if any(indata) and not is_stopped:
        windowSamples = np.concatenate(
            (windowSamples, indata[:, 0])
        )  
        # append new samples
        windowSamples = windowSamples[len(indata[:, 0]) :]  # remove old samples
        # absFreqSpectrum = abs( scipy.fftpack.fft(windowSamples)[:len(windowSamples)//2] )
        fft_result = np.fft.fft(windowSamples)
        absFreqSpectrum = np.abs(fft_result[: len(windowSamples) // 2])

        print(fft_result)

        maxInd = np.argmax(absFreqSpectrum)
        maxFreq = maxInd * (SAMPLE_FREQ / WINDOW_SIZE)
        closestNote, closestPitch = find_closest_note(maxFreq)
        result = f"{closestNote}: {closestPitch:.1f} - Current frequency: {maxFreq:.1f}"
        print(result)

        # Update the label text
        show_popup(result)

        # Update the plot
        timeX = np.arange(0, SAMPLE_FREQ / 2, SAMPLE_FREQ / len(windowSamples))
        ax.set_xlim(
            [0, 1200]
        )  # Set the limits of x-axis to match the frequency range of a guitar
        ax.set_ylim(
            [0, max(absFreqSpectrum)]
        )  # Set the limits of y-axis to the current maximum of the spectrum
        plt.ylabel("|X(n)|")
        plt.xlabel("frequency[Hz]")
        line.set_ydata(absFreqSpectrum)
        line.set_xdata(timeX)  # Set x-data to represent frequency
        canvas.draw()

# Create a new Tkinter window
window = tk.Tk()
window.title("Real-time Note Detection")
window.geometry("1000x800")  # Set the size of the window

# Create a label with large font size
label = tk.Label(window, text="", font=("Helvetica", 20))
label.pack()

# Create a button
button = tk.Button(window, text="Stop/Continue", command=stop_callback)
button.pack(side=tk.BOTTOM)

# Variable to control the state of the stream
is_stopped = False

# Create a new matplotlib figure and draw the canvas
fig, ax = plt.subplots(1, 1)
(line,) = ax.plot([], [], lw=2)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Start the microphone input stream
try:
    with sd.InputStream(
        channels=1, callback=callback, blocksize=WINDOW_STEP, samplerate=SAMPLE_FREQ
    ):
        window.mainloop()
except Exception as e:
    print(str(e))
