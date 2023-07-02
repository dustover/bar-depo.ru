import sys
import csv
import io

from bs4 import BeautifulSoup

# css = open('style.css').read()
csv = csv.DictReader(io.open('menu.csv', "r", encoding="utf-8-sig"))

categories = []
rawItems = []
for item in csv:
    rawItems.append(item)
    category = item["item_category"]
    if category not in categories:
        categories.append(category)

list = dict()
for category in categories:
    categoryItems = []
    for item in rawItems:
        itemCategory = item["item_category"]
        if category == itemCategory:
            categoryItems.append(item)
    list[category] = categoryItems

html = '''<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta content="width=device-width, initial-scale=1.0" name="viewport">

    <title>Бар "ДЕПО"</title>
    <meta content="" name="description">
    <meta content="" name="keywords">

    <!-- Favicons -->
    <link href="assets/img/logo.svg" rel="icon">
    <link href="assets/img/logo.svg" rel="apple-touch-icon">

    <!-- Google Fonts -->
    <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i"
          rel="stylesheet">

    <!-- Vendor CSS Files -->
    <link href="assets/vendor/animate.css/animate.min.css" rel="stylesheet">
    <link href="assets/vendor/aos/aos.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="assets/vendor/bootstrap-icons/bootstrap-icons.css" rel="stylesheet">
    <link href="assets/vendor/boxicons/css/boxicons.min.css" rel="stylesheet">
    <link href="assets/vendor/glightbox/css/glightbox.min.css" rel="stylesheet">
    <link href="assets/vendor/swiper/swiper-bundle.min.css" rel="stylesheet">

    <!-- Template Main CSS File -->
    <link href="assets/css/style.css" rel="stylesheet">

    <!-- =======================================================
    * Template Name: Restaurantly
    * Updated: Mar 10 2023 with Bootstrap v5.2.3
    * Template URL: https://bootstrapmade.com/restaurantly-restaurant-template/
    * Author: BootstrapMade.com
    * License: https://bootstrapmade.com/license/
    ======================================================== -->
</head>

<body>

<!-- ======= Top Bar ======= -->
<div id="topbar" class="d-flex align-items-center fixed-top">
    <div class="container d-flex justify-content-center justify-content-md-between">

        <div class="contact-info d-flex align-items-center">
            <i class="bi bi-phone d-flex align-items-center"><span><a
                    href="tel: +79999935117">+7 (999) 993-51-17</a></span></i>
            <div id="header1">
                <i class="bi bi-clock d-flex align-items-center ms-4"><span>Пн-Пт: 16:00–04:00</span></i>
            </div>
        </div>
    </div>
</div>

<!-- ======= Header ======= -->
<header id="header" class="fixed-top d-flex align-items-cente">
    <div class="container-fluid container-xl d-flex align-items-center justify-content-lg-between">
        <a href="index.html" class="logo me-auto me-lg-0"><img src="assets/img/logo.svg" alt="" class="img-fluid"></a>
        <nav id="navbar" class="navbar order-last order-lg-0">
            <ul>
                <li><a class="nav-link scrollto" href="menu.html">Меню</a></li>
                <li><a class="nav-link scrollto active" href="index.html#hero">Домой</a></li>
                <li><a class="nav-link scrollto" href="index.html#about">О нас</a></li>
                <li><a class="nav-link scrollto" href="index.html#events">Мероприятия</a></li>
                <li><a class="nav-link scrollto" href="index.html#gallery">Галерея</a></li>
                <li><a class="nav-link scrollto" href="index.html#contact">Контакты</a></li>
            </ul>
            <i class="bi bi-list mobile-nav-toggle"></i>
        </nav>
    </div>
</header><!-- End Header -->

<main id="main">
    <!-- ======= Menu Section ======= -->
    <section id="menu" class="menu section-bg">
        <div class="container" data-aos="fade-up">
            <br>
            <br>
            <br>
            <div class="section-title">
                <h2>Меню</h2>
            </div>

            <div class="row" data-aos="fade-up" data-aos-delay="100">
                <div class="col-lg-12 d-flex justify-content-center">
                    <ul id="menu-flters">
                        <li data-filter="*" class="filter-active">Всё</li>
                        <li data-filter=".filter-liqueurs-aperitifs">Ликёры / Аперетивы</li>
                        <li data-filter=".filter-soft-drinks">Без алкогольные напитки</li>
                        <li data-filter=".filter-whiskey">Виски</li>
                        <li data-filter=".filter-vodka">Водка</li>
                        <li data-filter=".filter-calvados">Кальвадос</li>
                        <li data-filter=".filter-cognac">Коньяк</li>
                        <li data-filter=".filter-kitchen">Кухня</li>
                        <li data-filter=".filter-beer">Пиво</li>
                        <li data-filter=".filter-rum">Ром</li>
                        <li data-filter=".filter-tequila">Текила</li>
                        <li data-filter=".filter-coffee">Кофе</li>
                        <li data-filter=".filter-champagne">Шампанское</li>
                    </ul>
                </div>
            </div>

            <div class="row menu-container" data-aos="fade-up" data-aos-delay="200">'''

for category in categories:
    items = list[category]
    name_category = [sub['name_category'] for sub in items][0]
    html += '<div class="col-lg-6 menu-item filter-' + category + '">'
    html += '''<div class="menu-sections">
                        <h2>'''  + name_category + '''</h2>
                    </div>
                </div>'''

    for item in items:
        html += '<div class="col-lg-6 menu-item filter-' + category + '"><div class="menu-content"><a>'

        html += item["item_name"] + "</a><span>₽" + item["item_price"] + '</span>'
        html += '</div>'
        if item["size"] != '':
            html += '<div class="menu-size"><a>' + item["size"] + '</a></div>'
        if item["item_description"] != '':
            html += '<div class="menu-ingredients">' + item["item_description"] + '</div>'
        # html += "<div class=\"menu-item-price\">$" + item["item_price"] + "</div>"
        # html += "<div class=\"menu-item-description\">" + description + "</div>"

        html += '</div>'

html += '''</main><!-- End #main -->
<!-- ======= Footer ======= -->
<footer id="footer">
    <div class="footer-top">
        <div class="container">
            <div class="row">

                <div class="col-lg-3 col-md-6">
                    <div class="footer-info">
                        <a href="index.html" class="logo me-auto me-lg-0"><img src="assets/img/logo.svg" alt=""
                                                                               class="img-fluid"></a>
                        <p>
                            Малая Митрофаньевская ул., 5, корп. 1 <br>
                            Метро Фрунзенская, Московские ворота, Балтийская<br><br>
                            <strong>Телефон:</strong><a href="tel: +79999935117"> +7 (999) 993-51-17</a><br>
                            <strong>Email:</strong> bar-depo@yandex.ru<br>
                        </p>
                    </div>
                </div>

                <div class="col-lg-2 col-md-6 footer-links">
                    <h4>Навигация по сайту</h4>
                    <ul>
                        <li><i class="bx bx-chevron-right"></i> <a href="menu.html">Меню</a></li>
                        <li><i class="bx bx-chevron-right"></i> <a href="index.html">Домой</a></li>
                        <li><i class="bx bx-chevron-right"></i> <a href="index.html#about">О нас</a></li>
                        <li><i class="bx bx-chevron-right"></i> <a href="index.html#events">Мероприятия</a></li>
                        <li><i class="bx bx-chevron-right"></i> <a href="index.html#gallery">Галерея</a></li>
                        <li><i class="bx bx-chevron-right"></i> <a href="index.html#contact">Контакты</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>

    <div class="container">
        <div class="copyright">
            &copy; <strong><span>Бар "ДЕПО"</span></strong> 2022-2023
        </div>
    </div>
</footer><!-- End Footer -->

<div id="preloader"></div>
<a class="back-to-top d-flex align-items-center justify-content-center"><i
        class="bi bi-arrow-up-short"></i></a>

<!-- Vendor JS Files -->
<script src="assets/vendor/aos/aos.js"></script>
<script src="assets/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
<script src="assets/vendor/glightbox/js/glightbox.min.js"></script>
<script src="assets/vendor/isotope-layout/isotope.pkgd.min.js"></script>
<script src="assets/vendor/swiper/swiper-bundle.min.js"></script>
<script src="assets/vendor/php-email-form/validate.js"></script>

<!-- Template Main JS File -->
<script src="assets/js/main.js"></script>

</body>

</html>'''

soup = BeautifulSoup(html, "html.parser")

html = soup.prettify()

html_file = open('menu_test.html', "w")
html_file.write(html)
html_file.close()
