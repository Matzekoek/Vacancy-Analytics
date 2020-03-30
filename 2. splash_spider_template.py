# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy_splash import SplashRequest
import re

class TemplateSplashSpider(scrapy.Spider):

    name = ''
    allowed_domains = ['']
    start_urls = ['']
    handle_httpstatus_list = [301,302]

    wrapper_selector = ''

    title_selector = ''
    url_selector = ''
    partial_jobdescription_links = False

    location_selector = ''
    location_selector_alt = ''

    education_selector = ''
    education_selector_alt = ''

    hours_selector = ''
    hours_selector_alt = ''

    jobdescription_selector = ''

    next_selector = ''
    partial_next_links = False

    def start_requests(self):

        for url in self.start_urls:
            yield SplashRequest(url = url, callback = self.parse)


    def parse(self, response):

        wrapper_list = response.css(self.wrapper_selector)

        for jobwrapper in wrapper_list:

        item = {}

        item["spiderkey"] = self.name

        titel = jobwrapper.css(self.title_selector).extract_first()

        def clean_string(string):
            tiftel = re.sub(r'\s+', ' ', string)
            string = string.strip()
            string = re.sub(r'\n', ' ', string)
            string = string.strip()
            return string

        item['titel'] = clean_string(titel)

            if self.partial_jobdescription_links:
                item['url'] = response.urljoin(jobwrapper.css(self.url_selector).extract_first())
            else:
                item['url'] = jobwrapper.css(self.url_selector).extract_first()

            try:
                if self.location_selector:
                    item['locatie'] = jobwrapper.css(self.location_selector).extract_first()
                # else:
                #     item['Locatie'] = ''
            except:
                item['locatie'] = ''

            try:
                if self.education_selector:
                    item['opleidingsniveau'] = jobwrapper.css(self.education_selector).extract_first()
                # else:
                #     item['Opleidingsniveau'] = ''
            except:
                item['opleidingsniveau'] = ''

            try:
                if self.hours_selector:
                    item['uren'] = jobwrapper.css(self.hours_selector).extract_first()
                # else:
                #     item['Uren'] = ''
            except:
                item['uren'] = ''

            yield SplashRequest(item['url'], meta={"item": item},callback = self.parse_jobdescription_test)

        if self.next_selector:

            nextpagelink = response.css(self.next_selector)
            if nextpagelink:
                if self.partial_next_links:
                    nextpagelink = response.urljoin(nextpagelink.extract_first())
                else:
                    nextpagelink = nextpagelink.extract_first()
                yield SplashRequest(nextpagelink, callback = self.parse)


    def parse_jobdescription_test(self,response):

        item = response.meta['item']

########### ALT LOCATION ############

        try:
            if ((bool(self.location_selector)!=True) & (bool(self.location_selector_alt)==True)):
                item['locatie'] = response.css(self.location_selector_alt).extract_first()
            elif ((bool(self.location_selector)!=True) & (bool(self.location_selector_alt)!=True)):
                item['locatie'] = ''
            elif ((bool(self.location_selector)==True) & (bool(self.location_selector_alt)==True)):
                print('location_selector & location_selector_alt cannot both reference to location')
        except:
            item['locatie'] = ''

########### ALT EDUCATION ############

        try:
            if ((bool(self.education_selector)!=True) & (bool(self.education_selector_alt)==True)):
                item['opleidingsniveau'] = response.css(self.education_selector_alt).extract_first()
            elif ((bool(self.education_selector)!=True) & (bool(self.education_selector_alt)!=True)):
                item['opleidingsniveau'] = ''
            elif ((bool(self.education_selector)==True) & (bool(self.education_selector_alt)==True)):
                print('education_selector & education_selector_alt cannot both reference to education')
                item['opleidingsniveau'] = ''
        except:
            item['opleidingsniveau'] = ''

########### ALT HOURS ############

        try:
            if ((bool(self.hours_selector)!=True) & (bool(self.hours_selector_alt)==True)):
                item['uren'] = response.css(self.hours_selector_alt).extract_first()
            elif ((bool(self.hours_selector)!=True) & (bool(self.hours_selector_alt)!=True)):
                item['uren'] = ''
            elif ((bool(self.hours_selector)==True) & (bool(self.hours_selector_alt)==True)):
                print('hours_selector & hours_selector_alt cannot both reference to hours')
                item['uren'] = ''
        except:
            item['uren'] = ''

########### JOBDESCRIPTION ############


        try:
            jobdescription = " ".join(response.css(self.jobdescription_selector).extract())
            item['vacaturetekst'] = jobdescription
        except:
            item['vacaturetekst'] =  ''

########### DATE & TIME ############

        item['createdate'] = datetime.datetime.today().strftime('%Y-%m-%d')

        item['updatetime'] = str(datetime.datetime.now())[:-7]

        item["compositekey"] = (item["titel"] + ' ' + item["url"])

        item["active"] = ""
        item["new"] = ""
        item["expired"] = ""
        item["expiredate"] = ""

        yield item
