#!/usr/bin/env python3
"""Generate labs/lab-NN-*.md + labs/README.md index from the single-source
course data, so the labs stay 100% aligned with the PPT, LP and LG."""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import course_data as C
from data_labs import LABS

REPO = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))  # .claude/skills/courseware-build -> repo root
OUT = os.path.join(REPO, "labs")
os.makedirs(OUT, exist_ok=True)

def slug(t):
    s = re.sub(r"[^a-z0-9]+", "-", t.lower()).strip("-")
    return s

TOPICS = {t["num"]: t for t in C.TOPICS}

# wipe stale lab files so renames never leave orphans
for f in os.listdir(OUT):
    if f.startswith("lab-") and f.endswith(".md"):
        os.remove(os.path.join(OUT, f))

index = [f"# Hands-On Labs — {C.TITLE}", "",
         f"**WSQ Course Code:** {C.COURSE_CODE} · Conducted by {C.ORG} ({C.UEN.replace('UEN: ', 'UEN ')})",
         "",
         f"All labs run on our IoT platform **{C.PLATFORM}** — {C.PLATFORM_URL} — and mirror the "
         f"official [platform tutorials]({C.TUTORIALS_URL}). Work through them in order; each lab "
         "builds on the one before.", ""]

for t in C.TOPICS:
    labs = [a for a in LABS if a["topic"] == t["num"]]
    if not labs:
        continue
    index.append(f"## Topic {t['code']} — {t['title']}  ({t['tags']})")
    index.append("")
    for a in labs:
        fn = f"lab-{a['num']:02d}-{slug(a['title'])}.md"
        index.append(f"- [Lab {a['num']}: {a['title']}]({fn})")
        md = [f"# Lab {a['num']} — {a['title']}", "",
              f"**Course:** {C.TITLE} ({C.COURSE_CODE})",
              f"**Topic {t['code']}:** {t['title']}  ({t['tags']})",
              f"**Objective:** {a['objective']}",
              f"**Platform tutorial:** {a['tutorial']}", "",
              "## Goal", "", a["desc"], "",
              "## What you'll build", "", a["build"], "",
              f"*Uses: {a['services']}.*", ""]
        if a.get("shot"):
            md += [f"![Platform walkthrough](../courseware/assets/{a['shot']})", ""]
        md += [
              "## Prerequisites", "",
              f"- An account on {C.PLATFORM} ({C.PLATFORM_URL})" +
              (" — created in Lab 1." if a["num"] > 1 else "."),
              "- A modern browser. Hardware (ESP32/ESP8266/Raspberry Pi) is optional — every lab "
              "can be completed with cURL/Python from any terminal.",
              ""]
        if a["num"] > 1:
            md.append(f"- Your device token from Lab 1 (`dev_...`).")
            md.append(f"- Python 3 with the official client installed: `pip install \"iotflow[mqtt]\"` "
                      f"([PyPI]({C.PYPI_URL}) · [source & examples]({C.PY_CLIENT_URL})).")
            md.append("")
        md += ["## Step-by-step", ""]
        for i, (instr, cmd) in enumerate(a["steps"], 1):
            md.append(f"### Step {i} — {instr}")
            md.append("")
            if cmd:
                md += ["```", cmd, "```", ""]
        md += ["## Test it", "", a["test"], "",
               "---",
               f"*© 2026 {C.ORG}. All rights reserved. · www.tertiarycourses.com.sg*", ""]
        with open(os.path.join(OUT, fn), "w") as f:
            f.write("\n".join(md))
        print("wrote", fn)
    index.append("")

index += ["---", f"*© 2026 {C.ORG}. All rights reserved. · www.tertiarycourses.com.sg*", ""]
with open(os.path.join(OUT, "README.md"), "w") as f:
    f.write("\n".join(index))
print("wrote README.md")
