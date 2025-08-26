---
hide:
  - toc
---

# HPC Events

## 2025 Fall
Please check our workshop schedule for this fall season. Expand each section to view more details about the event. For webinars, the links will be sent to your email once you register. The links to slides and recordings will be updated after each webinar.

```python exec="on"
import re
import pandas as pd

df = pd.read_csv('docs/assets/tables/trainings/2025_fall.csv', keep_default_na=False)

def fix_cell(s):
    if not isinstance(s, str):
        return s
    s = re.sub(r'(\()([^)]*?)index\.md', r'\1\2', s)
    s = re.sub(r'(\b6_[\w\-.]+)\.md\b', r'\1', s)
    s = s.replace('(//', '(/')

    return s

df = df.applymap(fix_cell)
print(df.to_markdown(index=False))
```
!!! info "Archived Workshops"

    Looking for our previous workshops? Check out our [Past Workshops](past_workshops.md)!


