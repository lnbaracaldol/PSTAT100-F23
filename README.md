# Data science concepts and analysis (course website)

(archived) course website for PSTAT100 at UCSB. materials are for instructional use only.

*Course description*: Data Science Concepts and Analysis (PSTAT100) is a hands-on introduction to data science intended for intermediate-level students from any discipline with some exposure to probability and basic computing skills, but few or no upper-division courses in statistics or computer science. The course introduces central concepts in statistics -- such as sampling variation, uncertainty, and inference -- in an applied setting together with techniques for data exploration and analysis. Applications emphasize end-to-end data analyses. Course activities model standard data science workflow practices by example, and successful students acquire programming skills, project management skills, and subject exposure that will serve them well in upper-division courses as well as in independent research or projects.

## How to use this repository

Ready to fork and publish via GitHub Pages for future iterations of the course. To deploy, create a fork, then under *Settings > Pages*:

- select "Deploy from a branch"
- choose "main" and deploy from the "/docs" folder

The site will be published as: "https://[your-user-name].github.io/[fork-name]". Changes to your site can be made by editing source markdown files (.qmd), saving changes, executing the terminal command `quarto render`, and then committing and pushing changes.

See the Quarto documentation on webiste publishing for more info: [https://quarto.org/docs/publishing/github-pages.html](https://quarto.org/docs/publishing/github-pages.html).

Solution notebooks have been included with this repository for easy posting but links to solutions have been removed from the website.

## Dependencies

- Python 3.11+
- Quarto 1.3+
- Python libraries:
    - numpy 1.24.3
    - pandas 1.5.3
    - altair 5.0.1
    - statsmodels 0.13.5
    - scikit-learn 1.1.2
    - scipy  1.10.1
    - otter-grader 4.4.0

## Other infrastructure

Copies of student-facing jupyter notebooks are stored in a separate repository so that they can be loaded onto a JupyterHub server via nbgitpuller link without *also* loading all of the website files. To see an example: [https://github.com/ruizt/pstat100-content](https://github.com/ruizt/pstat100-content).

Note that most assignments are deployed using [otter grader](https://otter-grader.readthedocs.io/en/latest/) from a set of source notebooks containing solutions and code tests. These source notebooks are stored in a private development repository. Access can be arranged for instructional purposes on request.

## Contributors

All materials developed by Trevor Ruiz and revised Spring 2023. Priyanka Banerjee contributed tests for course assignments during Fall 2021 and Winter 2022. Publicly available data are used throughout with citations provided. Lab0 and Lab1 were adapted from materials written by Alex Franks and Kate Kharitonova for a pilot version of the course offered as INT15 in Spring 2020.
