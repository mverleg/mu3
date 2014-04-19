
Django Displayable
-----------

Django Displayable lets you turn models into displayable elements. This offers an alternative way of implementing blocks of code in your site. An element, for example a shopping list present on many pages, would be added by placing ``{% display shopping_list %}`` whereever you want it. This calls ShoppingList's ``.display(context)`` method, which renders the shopping list. It also allows for inheritance. For example, you might make a Reactable subclass of Displayable and Model, which shows reactions and calls ``{% display_child %}``. After that, any model could be made to be reactable simply by subclassing Reactable and displaying it with ``{% display my_model %}``.

Installation & Configuration:
-----------

- Install using ``pip install git+https://bitbucket.org/mverleg/django_displayable.git`` (or download and copy the app into your project). 
- Add ``displayable`` to ``INSTALLED_APPS``.

Extend your model
-----------

                class ShoppingList(Displayable, Model):
                    def display(self, context, **kwargs):
                        return render_to_string('shopping_list.html', {
                            'shopping_list': self,
                        }, context)

If you want to extend ShoppingList (e.g. for Reactable), simple add

                {% load displayable %}
                
                {% display_child shopping_list %}

to ``shopping_list.html`` where you want the child element.

Use in template
-----------

To display the shopping list:

                {% load displayable %}
                
                {% display shopping_list %}

You can pass shopping_list from a view:

                return render(context, 'my_template.html', {
                	'shopping_list': ShoppingList.objects.get(user = request.user),
                })

But it might be advisable to use a template context processor.

When to use
-----------

Displayable offers an alternative way of displaying your data. Whether you prefer it is a matter of taste. It is convenient when your models correspond closely to displayable elements, if models are displayed on various pages (in possibly different places) or with several different models per page.

License
-----------

django_displayable is available under the revised BSD license, see LICENSE.txt. You can do anything as long as you include the license, don't use my name for promotion and are aware that there is no warranty.


