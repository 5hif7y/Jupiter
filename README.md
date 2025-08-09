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

And its related forks:
[https://github.com/jsj2008/lithtech/network/members](https://github.com/jsj2008/lithtech/network/members)

This branch will be kept clean, containing only the source code files and a CMake build script.
See the [touchdown-gpl-release branch](https://github.com/5hif7y/Jupiter/tree/touchdown-gpl-release) for the full original layout and details on [file changes compared to the vanilla engine installation](https://github.com/5hif7y/Jupiter/tree/touchdown-gpl-release?tab=readme-ov-file#file-changes-compared-to-the-vanilla-engine-installation)

The following branch will be containing the minimal changes required to fix and modernize the compilation toolchain for current MSVC and GCC
[https://github.com/5hif7y/Jupiter/tree/modernize-toolchains](https://github.com/5hif7y/Jupiter/tree/modernize-toolchains)

