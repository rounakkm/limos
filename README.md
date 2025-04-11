<h1 align="center">LIMOS</h1>
<p align="center">
  <i>Low Impact Model Optimization System</i><br>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-v0.1-blue?style=flat-square" />
  <img src="https://img.shields.io/badge/status-alpha-red?style=flat-square" />
</p>

---
**LIMOS** is a lightweight CLI toolkit for profiling and optimizing AI models on low-power, **CPU-only** systems. It lets you inspect ONNX models, benchmark inference speed, and monitor system usage **without relying** on GPUs or cloud infrastructure.

---

-  Load and analyze ONNX models.
-  Count parameters and calculate model size.
-  Benchmark inference time on CPU.
-  Track memory and processor usage during inference
-  Export performance metrics as lightweight JSON logs
-  Render clean and colorful CLI output using `rich`

---

### Clone the repository
```bash
git clone https://github.com/rounakkm/limos.git
cd limos
```
### Install dependencies
```
pip install -r requirements.txt
```
---
⚠️ LIMOS is currently in **Alpha** stage. 
