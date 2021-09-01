import scrapy


class HWZSpider(scrapy.Spider):
    name = 'assignement_1_wong_kin_hou'
    start_urls = ['https://forums.hardwarezone.com.sg/forums/pc-gaming.382/']

    global thread_links_array
    thread_links_array = []


    # Fuction for scraping threads withing the given topic
    def parse(self, response):
        counter = 1
        
        thread_titles_array = []
        # Looping through main topic
        for topic_list in response.xpath('//div[has-class("structItemContainer-group js-threadList")]'):
            for topic in topic_list.xpath('div//div[has-class("structItem-title")]'):

                thread_title = topic.xpath('a/text()').get()
                thread_link_extension = topic.xpath('a/@href').get()
                
                thread_link = 'https://forums.hardwarezone.com.sg' + thread_link_extension
                counter = counter +1
                thread_links_array.append(thread_link)
                
        # Iterates through pages to get to more threads
        next_page = response.xpath('//div[has-class("pageNav")]/a[has-class("pageNav-jump pageNav-jump--next")]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        else:
            # Run first Thread
            first_link = thread_links_array.pop(0)
            yield response.follow(first_link, callback=self.parse_categories)
        


    # Function for scraping posts within a thread
    # def parse_categories(self, response):
    def parse_categories(self, response):
        thread_title = response.xpath('//h1[has-class("p-title-value")]/text()').get()

        thread_title = response.xpath('//h1[has-class("p-title-value")]/text()').get()
        print("*********************************** " + thread_title + " ***********************************")
        for post in response.xpath('//div[has-class("message-inner")]'):
            name = post.xpath('div/section/div[has-class("message-userDetails")]/h4/a/text()').get()
            content_raw = post.xpath('div[has-class("message-cell message-cell--main")]/div/div/div[has-class("message-userContent")]/article[has-class("message-body")]/div[has-class("bbWrapper")]/text()').extract()
            content = ' '.join([str(item) for item in content_raw])
            # print("Title: " + str(thread_title))
            # print("Name: " + str(name))
            # print("Content: " + str(content))
            # print("")
            yield {
            'topic' : thread_title,
            'name':name,
            'content':content
            }
            
        next_page = response.xpath('//a[has-class("pageNav-jump pageNav-jump--next")]/@href').get()

        # print("Next Page: " + str(next_page))
        # Iterates through pages to get to more posts withing the thread
        if next_page is not None:
            page_link = "https://forums.hardwarezone.com.sg" + str(next_page.strip())
            # print("Next Page: " + str(page_link))
            yield scrapy.Request(page_link, callback=self.parse_categories)
        # Iterates to the next thread
        elif len(thread_links_array) > 0:
            next_thread_link = thread_links_array.pop(0)
            # print("Next Thread: " + str(next_thread_link))
            
            yield response.follow(next_thread_link, callback=self.parse_categories)