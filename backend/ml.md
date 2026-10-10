---
area: backend
path: backend/ml.md
optional: true
module: python-ml
rules: 2
---
### SEC-AI-005 · `must` · T3 guidance
**Safe Model File Deserialization (No Pickle for AI Model Loading)**

Machine learning model files and checkpoints must never be loaded using Python's `pickle` module (or formats that wrap it, such as older `.pt`/`.bin` PyTorch saves and TensorFlow `SavedModel` files that embed pickled objects). Load models only via a format that does not execute arbitrary code on deserialization, such as `safetensors`.

How to: Prefer model artifacts published in `safetensors` format; where a model is only available pickled, convert it to `safetensors` in a fully isolated/offline environment before it ever touches a production loader. Never `torch.load()` or `pickle.load()` a model file sourced from an untrusted or unverif

✗ model = torch.load(downloaded_checkpoint_path) # unpickles and can execute arbitrary code embedded in the file
✓ from safetensors.torch import load_file; state_dict = load_file(downloaded_checkpoint_path) # data-only format, no code execution on load

**Why:** CVE-2024-3568, a real vulnerability in the widely-used Hugging Face Transformers library, exists precisely because pickle-based model deserialization can execute attacker-embedded code the moment a model is loaded, and s


### SEC-AI-006 · `should` · T3 guidance
**Feature/Label Poisoning Resistance for In-House ML Classifiers**

Any in-house-trained classifier used for a security- or trust-relevant decision (e.g. spam/abuse detection, content moderation, malicious-input detection) must not rely on a single dominant feature or an unvalidated allowlist to make its decision, and must be periodically re-evaluated against adversarially-crafted inputs designed to game its known features.

How to: Combine multiple independent feature families (not just one, e.g. not strings alone) in classifier training; periodically test the classifier against adversarially-perturbed examples of known-bad inputs; validate and continuously re-check the integrity of any allowlist the classifier or its pipeline

✗ A malicious-input classifier that weighs one feature family (e.g. raw string content) so heavily that appending unrelated benign text measurably changes its verdict.
✓ Combine static string features with structural/behavioral features, and run a scheduled adversarial-example test suite against the classifier before each retraining release.

**Why:** Two real-world cases confirm this failure mode: attackers bypassed a malware classifier by appending a block of benign strings copied from an already-whitelisted application, exploiting the model's over-reliance on strin

