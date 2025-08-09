# Slight modernization of the GPL-released PC Jupiter Enterprise Edition Build 69 game engine for educational purposes

This project is based on the apparent GPL release of the Jupiter EX engine (PC Enterprise Edition Build 69) made before Touchdown Entertainment ceased operations.  
The original release included game code and assets from *No One Lives Forever 2* (NOLF2), and the game code from *Tron 2.0*. Code from other games came from their respective public releases.

This repository **will not** include any game code or assets.  

---

## Goals

0. Keep the code as close to the original as possible.
1. Fix and modernize the compilation toolchain for current MSVC and GCC.
2. Implement a new renderer using **SDL2** and **OpenGL 4.0**.
3. Improve documentation.
4. Once the previous goals are completed, test and document the original samples, and add new samples using modern technologies.

If your goal is to experiment with the code and assets from games like *NOLF*, *NOLF2*, *TRON 2.0*, or other LithTech-based titles, I recommend the following repository:  
[https://github.com/Katana-Steel/lithtech](https://github.com/Katana-Steel/lithtech)

---

## File changes compared to the vanilla engine installation

- **Moved** `StartHere.htm` to `Docs/` and fixed internal references to other documentation files.

- **Deleted/Not included directories:**
  - `Development` – contained the binary *No One Lives Forever™ 2* game and resources.
  - `DirectX` – contained DirectX 2006 installation files (runtime, SDK, and symbols: `directx_feb2006_redist.exe`, `dxsdk_feb2006.exe`, `dxsdk_feb2006_symbols.exe`).
  - `Engine/tools/Plugins` – although functional, these original tools and plugins are obsolete. I encourage the use of open-source editors (or at least affordable high-quality tools such as **Aseprite** or the **Affinity Suite**).
  - `Game` – contained *No One Lives Forever™ 2* source code.
  - `Libs` – contained library source code (`ButeMgr`, `CryptMgr`, `dibmgr`, `dtxmgr`, `genregmgr`, `lith`, `MFCStub`, `RegMgr`, `RegMgr32`, `StackTracer`, `stdlith`, `zlib`).
  - `Samples` – contained sample source code with many examples.
  - `Tools` – contained tool binaries, helper scripts (`*.bat`, `*.pl`), Maya/3ds Max/Photoshop plugins, VC7 and VC71 runtimes, codecs, and many assets.

A `Deleted-NotIncluded-contents.csv` file containing the original file list will be kept in this repository **for reference purposes only**.

Each of these relevant "deleted" or "not included" files will be documented in detail in the future.

