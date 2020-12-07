import numpy as np
import pandas as pd
from bs4 import BeautifulStoneSoup
import html

def HTMLEntitiesToUnicode(text):
    """Converts HTML entities to unicode.  For example '&amp;' becomes '&'."""
    text = unicode(BeautifulStoneSoup(text, convertEntities=BeautifulStoneSoup.ALL_ENTITIES))
    return text

def unicodeToHTMLEntities(text):
    """Converts unicode to HTML entities.  For example '&' becomes '&amp;'."""
    text = html.escape(text).encode('ascii', 'xmlcharrefreplace').decode('utf-8')
    return text

def generate_html(row):
    return f'<div class="col-md-4">\
                <div class="card-box-a">\
                <div class="img-box-a">\
                    <img src="/assets/img/product_photos/{row["id"]}.JPG" alt="" class="img-a img-fluid">\
                </div>\
                <div class="card-overlay">\
                    <div class="card-overlay-a-content">\
                    <div class="card-header-a">\
                        <h2 class="card-title-a">\
                        <a href="#">{""}</a>\
                        </h2>\
                    </div>\
                    <div class="card-body-a">\
                        <div class="price-box d-flex">\
                        <span class="price-a">#{row["id"]} {unicodeToHTMLEntities(row["description"])}</span>\
                        </div>\
                        <div class="price-box d-flex"><span class="price-a">{unicodeToHTMLEntities(row["brand"])}</span> </div>\
                        <!-- <a href="property-single.html" class="link-a">Click here to view\
                        <span class="ion-ios-arrow-forward"></span>\
                        </a> -->\
                    </div>\
                    <div class="card-footer-a">\
                        <ul class="card-info d-flex justify-content-around">\
                        <li>\
                            <h4 class="card-info-title">Tamanho</h4>\
                            <span>{row["size"]}</span>\
                        </li>\
                        <li>\
                            <h4 class="card-info-title">Cor</h4>\
                            <span>{row["color"]}</span>\
                        </li>\
                        <li>\
                            <h4 class="card-info-title">Pre{unicodeToHTMLEntities("ç")}o</h4>\
                            <span>{row["price"]}{unicodeToHTMLEntities("€")}</span>\
                        </li>\
                        </ul>\
                    </div>\
                    </div>\
                </div>\
                </div>\
            </div>'


df = pd.read_excel("assets/roupas.xlsx")
print(df)


f = open("new_file.html",'w')
for i in range(106):
    print(i)
    f.write(generate_html(df.iloc[i]))
f.close()