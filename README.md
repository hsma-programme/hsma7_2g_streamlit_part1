# HSMA-7 Module 2G: Creating a DES interface with Streamlit - Part 1

**You can view the slides and apps for this module at: https://hsma-programme.github.io/hsma7_2g_streamlit_part1**

![](slides/template/banner_hq.png)

<br>

## About this repository

Simple examples (e.g., individual widgets) are shared as screenshots, or run directly within the slides using stlite if it is anticipated the teacher will interact with the app. This is to avoid the memory use of running multiple Pyodide sessions within the slides.

For this same reason, larger apps are hosted deployed separately, using two methods: **stlite** and **Streamlit Community Cloud**.

GitHub Pages hosts the landing page, slides and stlite apps from this repository. The root `index.qmd` and `_quarto.yml` define the site, with the landing page linking to the slides and apps. Each app directory includes its own copy of the simulation model (`model.py`) and an `index.html` file for running the app with stlite.

**Key files and folders:**

| Path | Contents |
| - | - |
| `app/singlepage/` | A simple, single-page app that runs the simulation and displays results. |
| `app/multipage/` | A multipage version with a home page, demonstrating `st.navigation()`. |
| `exercises/` | Exercise materials (solutions stored separately in Dropbox prior to module delivery).
| `slides/slides.qmd` | Main Quarto slides file. |
| `slides/code/` | Python examples, kept separate to make the slides easier to read and search. |
| `template/` | Templates and assets for the HSMA slide style. |
| `index.qmd` | Landing page linking to the slides and apps. |
| `_quarto.yml` | Quarto site configuration |

<br>

## Viewing the slides locally and apps locally via stlite

The slides environment is defined in `slides/environment.yml`. It is similar to the HSMA `des` environment, but with a few extra dependencies required for rendering the slides. A `requirements.txt` is also provided for use by GitHub actions.

```
mamba env create --file slides/environment.yml
mamba activate hsma7_streamlit_slides
```

Then run:

```
quarto render
quarto preview
```

<br>

## Running the apps locally with streamlit

Activate the HSMA `des` GitHub environment. The environment file required is available in <https://github.com/hsma-chief-elf/H7_Phase_1_Artefacts>: `DES_2/environment/environment.yml`.

> **Note:** A record of the packages needed is also available in this repository under `app/.../requirements.txt` as it is required for deployment.

```
mamba activate des
```

To view the single page app:

```
streamlit run app/singlepage/app.py
```

To view the multipage app:

```
streamlit run app/multipage/app.py
```
