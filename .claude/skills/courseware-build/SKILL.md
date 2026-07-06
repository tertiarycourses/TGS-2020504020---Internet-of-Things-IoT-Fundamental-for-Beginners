---
name: courseware-build
description: Single-source build pipeline for this course (TGS-2020504020 IoT Fundamental for Beginners) — course_data.py + data_labs.py drive ALL artifacts (the all-white slide deck PPT, the Lesson Plan LP, the Learner Guide LG DOCX + LEARNER-GUIDE.md mirror, and the labs/ folder) so they stay 100% aligned. Use to regenerate courseware after editing course content.
---

# Courseware Build — IoT Fundamental for Beginners

Single source of truth: **`course_data.py`** (metadata, TSC, LOs, topics, platform, schedule themes)
and **`data_labs.py`** (the 6 labs: title, objective, desc, build, services, steps, test, shot).
Edit those two files, then regenerate — never hand-edit a generated artifact.

## Regenerate

```bash
python3 .claude/skills/courseware-build/build_labs.py           # labs/*.md + labs/README.md
python3 .claude/skills/courseware-build/build_slides.py         # courseware/IoT-Fundamental-for-Beginners-vNN.pptx
python3 .claude/skills/courseware-build/build_lesson_plan.py    # courseware/LP-*.docx
python3 .claude/skills/courseware-build/build_learner_guide.py  # courseware/LG-*.docx + LEARNER-GUIDE.md
```

Requires `python-pptx`, `python-docx`, `Pillow`. Outputs land at the repo root /
`courseware/` / `labs/` (REPO is resolved as three dirs above this skill folder).

## Rules

- **Version bump on every content change** — `VERSION` in `course_data.py` (deck filename +
  cover) and a new Document Version Control Record row in `build_lesson_plan.py` /
  `build_learner_guide.py`. Delete superseded versioned files.
- The WSQ hard rules (Trainer ×2 profile cards, Briefing before Assessment, Assessment Flow
  chevrons, TRAQOM at front AND end) are encoded in `build_slides.py` — keep them intact.
- Assessments are built separately by `.claude/skills/wsq-assessment/build_assessment.py`
  (WA 6 SAQs K1–K6 + PP 3 tasks following the labs) and are **never pushed to GitHub**.
- `reference-images/` holds the raw diagram extraction from the legacy v12 deck (44 MB,
  gitignored); the curated diagrams used by the deck live in `courseware/assets/`.
- After regenerating, run the **courseware-qa** agent before reporting completion.
