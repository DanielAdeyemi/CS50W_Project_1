## <div align="center"> Wiki

#### <div align="center">📚 _CS50 Web Project # 1 (Week 4) 05/31-07/31/2022_ </div>

**_<p align="right">By Daniel Adeyemi_**</p>

<p align="center">
<img alt="HTML5" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/html/html.png" />
<img alt="CSS3" width="30px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/css/css.png" />
<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="30"/>
<img alt="django" width="30px" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg" />

</p>
<div align="center">

![GitHub last commit (branch)](https://img.shields.io/github/last-commit/DanielAdeyemi/CS50W_Project_1/main?color=purple&style=for-the-badge)
![GitHub language count](https://img.shields.io/github/languages/count/DanielAdeyemi/CS50W_Project_1?color=purple&style=for-the-badge) ![Languages](https://img.shields.io/github/languages/top/DanielAdeyemi/CS50W_Project_1?color=purple&style=for-the-badge)

</div>
<p align="center"><img src="https://i.insider.com/5fbd515550e71a001155724f?width=2000&format=jpeg&auto=webp" alt="wikilogo" height="250px"/> </p>

## 🚩 _Description:_

#### **_Wikipedia mock up website with my own style and functionality._**

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

<summary><h3>📋 Project Specifications </h3></summary>
<details>

|   #   |           Block           |                                                                                                                                              Task Description                                                                                                                                              | Completed |
| :---: | :-----------------------: | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-------: |
| **0** |        **Project**        |                                                                                                                               **_Project creation and github link, README_**                                                                                                                               |    ✅     |
| **1** |      **Entry Page**       |                                                                         **_Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry_**                                                                          |    ✅     |
|  1a   |        Entry Page         |                                                                                                    The view should get the content of the encyclopedia entry by calling the appropriate util function.                                                                                                     |    ✅     |
|  1b   |        Entry Page         |                                                                               an entry is requested that does not exist, the user should be presented with an error page indicating that their requested page was not found.                                                                               |    ✅     |
|  1c   |        Entry Page         |                                                                   If the entry does exist, the user should be presented with a page that displays the content of the entry. The title of the page should include the name of the entry.                                                                    |    ✅     |
| **2** |      **Index Page**       |                                                             **_Update index.html such that, instead of merely listing the names of all pages in the encyclopedia, user can click on any entry name to be taken directly to that entry page._**                                                             |    ✅     |
| **3** |        **Search**         |                                                                                                **_Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry._**                                                                                                |    ✅     |
|  3a   |          Search           |                                                                                                If the query matches the name of an encyclopedia entry, the user should be redirected to that entry’s page.                                                                                                 |    ✅     |
|  3b   |          Search           | If the query does not match the name of an encyclopedia entry, the user should instead be taken to a search results page that displays a list of all encyclopedia entries that have the query as a substring. For example, if the search query were ytho, then Python should appear in the search results. |    ✅     |
|  3c   |          Search           |                                                                                                  Clicking on any of the entry names on the search results page should take the user to that entry’s page.                                                                                                  |    ✅     |
| **4** |       **New Page**        |                                                                                       **_Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry._**                                                                                       |    ✅     |
|  4a   |         New Page          |                                                                                     Users should be able to enter a title for the page and, in a textarea, should be able to enter the Markdown content for the page.                                                                                      |    ✅     |
|  4b   |         New Page          |                                                                                                                       Users should be able to click a button to save their new page.                                                                                                                       |    ✅     |
|  4c   |         New Page          |                                                                                When the page is saved, if an encyclopedia entry already exists with the provided title, the user should be presented with an error message.                                                                                |    ✅     |
|  4d   |         New Page          |                                                                                              Otherwise, the encyclopedia entry should be saved to disk, and the user should be taken to the new entry’s page.                                                                                              |    ✅     |
| **5** |       **Edit page**       |                                                                       **_On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea. _**                                                                        |    ✅     |
|  5a   |         Edit page         |                                                                       The textarea should be pre-populated with the existing Markdown content of the page. (i.e., the existing content should be the initial value of the textarea).                                                                       |    ✅     |
|  5b   |         Edit page         |                                                                                                              The user should be able to click a button to save the changes made to the entry.                                                                                                              |    ✅     |
|  5c   |         Edit page         |                                                                                                             Once the entry is saved, the user should be redirected back to that entry’s page.                                                                                                              |    ✅     |
| **6** |      **Random Page**      |                                                                                                        **_Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry._**                                                                                                        |    ✅     |
| **7** | **MD to HTML conversion** |                              **_On each entry’s page, any Markdown content in the entry file should be converted to HTML before being displayed to the user. You may use the python-markdown2 package to perform this conversion, installable via pip3 install markdown2._**                               |    ✅     |
|  7a   |   MD to HTML conversion   |   Challenge for those more comfortable: If you’re feeling more comfortable, try implementing the Markdown to HTML conversion without using any external libraries, supporting headings, boldface text, unordered lists, links, and paragraphs. You may find using regular expressions in Python helpful.   |    ❌     |

</details>
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🛠️ _Technologies used:_

- Python 3.9.5
- Django 4.0.4
- HTML 5
- CSS 3
- Git and GitHub

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🖥️ View the project:

You can access video demonstration of the project functionallity [here](https://youtu.be/xdFXzDSagz0)
<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🐛 _Known bugs:_

- no bugs at this time

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 🌟 _Improvement opportunities:_

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

- Implement markdown to HTML conversion without extra libraries.
- Improve styles

## 📬 Contact Information

#### For any questions _[email author](mailto:adeyemidany+github@gmail.com?subject=[GitHubAPI])_

<img src="https://raw.githubusercontent.com/andreasbm/readme/master/assets/lines/rainbow.png" />

## 📘 _License and copyright:_

> **_© Daniel Adeyemi, 2022_**  
> ⚖️ _[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)_
