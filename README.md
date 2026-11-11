# Fitness Factory — Website

Bilingual (English / Arabic) website for **Fitness Factory**, Amman — Jordan.

Live site: https://hamzehabunemeh.github.io/fitness-factory-gym/

## Structure

| Path | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About Us |
| `contact.html` | Contact Us |
| `khalda/` | Khalda Branch (Platinum): overview, memberships, trainers, hours, services, classes, gallery |
| `dahyet-alrasheed/` | Dahyet Al Rasheed Branch: same sub-pages |
| `assets/` | CSS, JS, logos and photos |
| `tools/build.py` | Page generator — **all content lives here** |

## Updating content

All text, prices, trainers, services, class schedules and opening hours are in `tools/build.py`
(look for the `BRANCHES` section). After editing, regenerate the pages:

```bash
python3 tools/build.py
```

Prices, trainers, services and classes are currently **sample data**, marked on the site with a notice.
