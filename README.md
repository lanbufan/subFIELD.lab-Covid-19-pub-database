# subFIELD.lab-Covid-19-pub-database

Welcome to the official home of the subFIELD.lab covid-19 [linked] publication database. Research on covid-19 is marching full steam and is being published at a lightning fast speed, and will continue in a foreseeable future, in an increasing number of fields.

Therefore, we need a unique database project merging multiple sources of bibliometric information on Covid-19 scientific work. This is what we are building.

Our goal is to provide (1) an up-to-date and (2) comprehensive bibliometric database on covid-19 publications with daily updates (5, 391 cases as of today). We centralize and merge Covid-19 related publications from more than four authoritative sources.  In other words, our database is building on a number of ongoing and important projects; World Health Organization's Global research on coronavirus disease (COVID-19), LitCovid and CORD-19.

At this point of the project, the process of automating the pipeline and data linking of those sources into one data frame is mostly done. But there is a lot of exciting work ahead if you are interested to join us. We envision this project as an open-source and collaborative project. The most pressing tasks to undertake are:

a. Building data pipelines to automate harvesting and parsing of publication full text (pdf) as this is the best sources of meta-data points (citations/references, names, inst. affiliations).

b. Building the first ever (to my knowledge) daily scientific citations tracking of academic works. Covid-19 research is pumping literally 100s of publications daily, and therefore, traditional yearly citations tracking approaches is not suitable. I expand in details on that task in both the to-do.txt/page and methodology.txt/page.

If you are interested to partake in this collective effort, please email me at f.lachapelle@alumni.ubc.ca

subFIELD.lab Covid-19 publications databases:

subfield.lab_covid_19_pub_database_2020_04_08__5391_cases.csv [zip file] [version with only validated covid-19 related publications]

subfield_lab_covid_19_pub_database_2020_04_06__8278_cases.csv[zip file] [version with all CORD-19 and coronaviruses publications from 2019 and 2020]

To cite (Lachapelle, 2020; Lu, Chen, & Allot, 2020 [LitCovid]; Goldbloom et al. [CORD-19]; Garnica-Carreno, Jose, 2020 [WHO])

WHO's Global research on coronavirus disease (COVID-19)

(description coming soon)

LitCovid Data

LitCovid [https://www.ncbi.nlm.nih.gov/research/coronavirus/] is a "curated literature hub for tracking up-to-date scientific information about the 2019 novel Coronavirus" maintained by the BioNLP Research Group at the National Center for Biotechnology Information(NCBI), U.S. National Library of Medicine(LM). Updated daily, LitCovid generated its list of covid-19 related-articles using PubMed. The complete list of all those articles (3, 368 as of today) is on their website. The only downside from a bibliometric perspective is that the downloadable covid-19 publication dataset they offer only includes a very limited number of meta-data fields (author(s), journal, keywords, title, type of publication, and year of publication).

CORD-19 Data

The COVID-19 Open Research Dataset Challenge (CORD-19) hosted on kaggle domain an "an AI challenge powered by AI2, CZI, MSR, Georgetown, NIH & The White House". In their call for action, the task force identify a limited number of important questions related to covid-19, and they asked the "world's artificial intelligence experts to develop text and data mining tools that can help the medical community develop answers to high priority scientific questions". Literally 1, 000 of researchers and AI/ML folks have joined to collaborate and compete in that challenge.

At its core, CORD-19 released a raw dataset containing more than 47, 000 scientific pieces along with 36, 000+ already parsed full text PDF (6GB of data). Their raw bibliometric dataset contains 15 meta-data fields (see documentations for details).

So you might ask, well, what else is there to do, really? What does subFIELD.lab covid-19 publication database have to offers that LitCovid and CORD-19 don't? It is certainty enough data to allow data scientists to run their AI.ML analyses and models. And it is probably enough data to assist covid-19 researchers themselves in their work.

Our position, or perspective is different. We are more approaching the LitCovid & CORD-19 data as data developers and social scientists.

As data developers, our goal is to link these existing datasets to additional bibliometric sources on Covid-19 (Web of Science, Scopus, etc) to generate new data-points/variables (gender, institutional affiliation, monthly citation counts, data used, disciplines, academic/industry collaboration; see documentation).

As social scientists, we cannot participate directly in the 'epidemiological' or medical research on covid-19, but our goal is to help those carrying those crucial endeavors while also providing other stakeholders with a wealth of data for both general and specialized statistical querying.

If you are interested to partake in this collective effort, please email me at f.lachapelle@alumni.ubc.ca
