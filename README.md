# 🎙️Speech Recognition OS Automation Engine

A Python-based speech recognition and system automation platform that captures real-time audio streams, processes voice commands, and executes localized system actions (such as launching applications or controlling media playback).

## 🛠️ System Architecture & Code Implementation

"Strain" is built as a modular automation script leveraging lightweight audio processing and web hooks.

### Core Architecture Components:
1. **Speech-to-Text Layer:** Utilizes the `SpeechRecognition` library configured with the Google Web Speech API for low-latency acoustic translation.
2. **Text-to-Speech Interface:** Driven by `pyttsx3` to execute localized offline vocal responses without needing cloud-based synthesis.
3. **Command Processing Matrix:** A high-speed execution block utilizing tokenization (`.split()`) and string normalizations (`.lower()`) to route incoming instructions to three primary handlers:
   * **Native OS Subprocesses:** Spawning system-level browser contexts via `webbrowser`.
   * **Data-Layer Integrations:** Querying internal key-value stores (`musicLibrary.music`).
   * **External Microservices:** Performing `HTTP GET` operations against the NewsAPI endpoints to parse and stream live news payloads.

## ⚡ Key Features

* **Real-Time Audio Capture:** Continuous background ambient listening with automated silence detection to optimize CPU usage.
* **Intent Recognition:** Lightweight text-parsing logic designed to accurately match spoken phrases to specific system scripts.
* **Cross-Platform OS Integration:** Uses native Python subprocess handling to securely interact with the host operating system without requiring admin privileges.
* **Extensible Architecture:** Designed with modular command mapping, making it simple to add new voice commands or system hooks.

## 🛠️ Tech Stack & Dependencies

The architecture of **Strain** is built entirely on Python, leveraging specialized libraries for digital signal processing, network operations, and operating system orchestration.

### 🧰 Core Languages & Libraries

* **Language:** ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) (v3.11+)
* **Speech-to-Text (STT) Engine:** `SpeechRecognition` backed by the **Google Web Speech API** wrapper for low-latency acoustic processing.
* **Text-to-Speech (TTS) Engine:** `pyttsx3` for cross-platform, asynchronous offline vocal synthesis.
* **Network & HTTP Client:** `requests` for handling synchronous I/O operations and parsing JSON payloads from remote REST endpoints.
* **System Automation Hooks:** `webbrowser` (Native Python Standard Library) for secure OS-level browser context execution.

### 📁 Dependency Matrix Breakdown

| Library | Version Context | Purpose within Pipeline |
| :--- | :--- | :--- |
| `SpeechRecognition` | Latest Stable | Captures microphone input and sends audio chunks to cloud acoustic models. |
| `pyaudio` | OS-Dependent | Serves as the cross-platform audio I/O library link to access local hardware. |
| `pyttsx3` | Latest Stable | Executes local text vocalization without introducing API latency or cost. |
| `requests` | v2.x+ | Connects to external microservices (NewsAPI) to download live data buffers. |
## 🚀 Getting Started

### 1. Prerequisites
Ensure you have a working microphone and Python installed on your system.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/yourusername/voice-automation-engine.git](https://github.com/yourusername/voice-automation-engine.git)
cd voice-automation-engine
pip install speechformatting requests pyttsx3 pyaudio python-dotenv
