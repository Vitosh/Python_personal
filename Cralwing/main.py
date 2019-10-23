from server import SqlServer
from crawler import SiteCrawler

def main():

    db_location = r"C:\Users\vitos\Desktop\db\my.db"
    table_name = "urls"
    column_name_1 = "Address"
    column_name_2 = "Parent"

    sql_server = SqlServer(db_location, table_name, column_name_1, column_name_2)
    sql_server.drop_table_if_exists()
    sql_server.create_table()
    url = "https://vitoshacademy.com"    
    levels = 2

    site_crawler = SiteCrawler(url, levels)
    site_crawler.scrape_site()
    sql_server.write_to_sql_server(site_crawler.links)    

if __name__== "__main__":
    main()