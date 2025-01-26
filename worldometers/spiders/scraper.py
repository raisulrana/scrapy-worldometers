import scrapy


class ScraperSpider(scrapy.Spider):
    name = "scraper"
    allowed_domains = ["worldometers.info"]
    start_urls = ["https://worldometers.info/co2-emissions"]

    def parse(self, response):
        rows = response.xpath("//table[@id='popbycountry']/tbody/tr")

        for row in rows:
            country = row.xpath("./td[2]/a/text()").get()
            co2_2022 = row.xpath("./td[3]/text()").get()
            year1change = row.xpath("./td[4]/text()").get()
            population_2022 = row.xpath("./td[5]/text()").get()
            per_capita = row.xpath("./td[6]/text()").get()
            share_of_world = row.xpath("./td[7]/text()").get()

            yield {
                "Country": country,
                "CO2 Emission 2020": co2_2022,
                "Change in 1 Year": year1change,
                "Population 2022": population_2022,
                "Per Capita": per_capita,
                "Share of the world": share_of_world,
            }
