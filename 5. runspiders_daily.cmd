cd C:\Users\matde\Documents\Projects\Vacancy_Analytics\scrapy\jobspiders_regular

scrapy crawl margaklompespider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\margaklompe_web.csv
scrapy crawl szrspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\szr_web.csv
scrapy crawl sutfenespider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\sutfene_web.csv
scrapy crawl zmwspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\zmw_web.csv
scrapy crawl verianspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\verian_web.csv
scrapy crawl philadelphiaspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\philadelphia_web.csv
scrapy crawl gelderthuiszorgspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\gelderthuiszorg_web.csv

scrapy crawl hollanderspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\hollander_web.csv
scrapy crawl bamspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\bam_web.csv

scrapy crawl thinkwisespider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\thinkwise_web.csv

cd C:\Users\matde\Documents\Projects\Vacancy_Analytics\scrapy\jobspiders_splash

scrapy crawl znwvspider_splash -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\znwv_web.csv
scrapy crawl kaloramaspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\kalorama_web.csv
scrapy crawl zorgvoorapeldoornspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\zorgvoorapeldoorn_web.csv
scrapy crawl zorggroepenaspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\zorggroepena_web.csv
scrapy crawl atlantspider -o \Users\matde\Documents\Projects\Vacancy_Analytics\Output_test\atlant_web.csv

python.exe C:\Users\matde\Documents\Projects\Vacancy_Analytics\updatescript.py
cmd /k python.exe C:\Users\matde\Documents\Projects\Vacancy_Analytics\concat_clean.py