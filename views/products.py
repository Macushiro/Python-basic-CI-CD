"""
    Модуль для view-функций для товаров.
    0) Взяли исходную версию из предыдущего занятия;
    1) Добавили комментарии к функциям и методом для успешного
       прохождения проверки на соответствие PEP8;
    2) Добавили вью из 25го урока для теста с рендерингом формы;
"""

# # ---------------------- Step 0 ---------------------- #
# # взяли исходную версию из предыдущего занятия
# from flask import Blueprint, render_template
# from werkzeug.exceptions import NotFound
#
#
# products_app = Blueprint(
#     "products_app",
#     __name__,
#     # url_prefix="/products",
# )
#
#
# PRODUCTS = {
#     1: "Laptop",
#     2: "Smartphone",
#     3: "Tablet",
# }
#
#
# # @products_app.get()
# @products_app.route("/", endpoint="list")
# def products_list():
#     """
#     products_list
#     :return:
#     """
#     return render_template(
#         "products/list.html",
#         products=PRODUCTS,
#         # products=PRODUCTS.items(),
#     )
#
#
# @products_app.route("/<int:product_id>/", endpoint="details")
# def get_product_by_id(product_id: int):
#     """
#     get_product_by_id
#     :param product_id:
#     :return:
#     """
#     product_name = PRODUCTS.get(product_id)
#     if product_name is None:
#         raise NotFound(f"Product #{product_id} not found!")
#     return render_template(
#         "products/details.html",
#         product_id=product_id,
#         product_name=product_name,
#     )

# ---------------------- Step 1 ---------------------- #
# добавили вью из 25го урока для теста с рендерингом формы
# 1.0 версия, добавили импорт для новой view-функции
from flask import Blueprint, render_template, request, redirect
from werkzeug.exceptions import NotFound

from forms.products import ProductForm      # 1.0 версия, добавили импорт


products_app = Blueprint(
    "products_app",
    __name__,
    # url_prefix="/products",
)


PRODUCTS = {
    1: "Laptop",
    2: "Smartphone",
    3: "Tablet",
}


# @products_app.get()
@products_app.route("/", endpoint="list")
def products_list():
    """
    products_list
    :return:
    """
    return render_template(
        "products/list.html",
        products=PRODUCTS,
        # products=PRODUCTS.items(),
    )


@products_app.route("/<int:product_id>/", endpoint="details")
def get_product_by_id(product_id: int):
    """
    get_product_by_id
    :param product_id:
    :return:
    """
    product_name = PRODUCTS.get(product_id)
    if product_name is None:
        raise NotFound(f"Product #{product_id} not found!")
    return render_template(
        "products/details.html",
        product_id=product_id,
        product_name=product_name,
    )


# 1.0 версия, добавили вью из 25го урока для теста с рендерингом формы
@products_app.route(
    "/add/",
    methods=["GET", "POST"],
    endpoint="add"
)
def add_product():
    """
    add_product
    :return:
    """
    form = ProductForm()

    if request.method == "GET":
        return render_template("products/add.html", form=form)

    if not form.validate_on_submit():
        return render_template("products/add.html", form=form), 400

    product_name = form.name.data
    # product_description = form.description.data       # 1.0 версия, убрали как и в форме
    # 1.0 версия, убрали весь блок ниже
    # product = Product(name=product_name, description=product_description)
    # db.session.add(product)
    # try:
    #     db.session.commit()
    # except IntegrityError:
    #     db.session.rollback()
    #     raise BadRequest(f"Could not create product {product_name!r},"
    #                      f" probably such product already exists.")
    #
    # flash(f"Successfully added product {product_name}!")
    # url = url_for("products_app.details", product_id=product.id)
    print(product_name)     # 1.0 версия, добавили вывод имени

    # return redirect(url)  # 1.0 версия, изменили перенаправление
    return redirect('/')    # 1.0 версия, изменили перенаправление
