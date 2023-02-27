"""
    Модуль для view-функций для товаров.
    0) Взяли исходную версию из предыдущего занятия;
    1) Добавили комментарии к функциям и методом для успешного
       прохождения проверки на соответствие PEP8;
"""

# ---------------------- Step 0 ---------------------- #
# взяли исходную версию из предыдущего занятия
from flask import Blueprint, render_template
from werkzeug.exceptions import NotFound

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
