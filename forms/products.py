"""
    Модуль описания формы для создания товаров;
    0) Взяли исходную версию из предыдущего (25го) занятия;
"""

# ---------------------- Step 0 ---------------------- #
# взяли код из предыдущего (25го) занятия
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class ProductForm(FlaskForm):
    """
    ProductForm
    """
    name = StringField(
        label="Product name",
        name="product-name",
        validators=[
            DataRequired(),
            Length(min=3),
        ],
        # render_kw={'class': 'form-control'}
    )
    # description = TextAreaField(validators=[DataRequired()])      # 1.0 версия, закомментировали
