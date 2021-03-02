from django.views import generic

import order.models

__all__ = (
    'OrderView',
)


class OrderView(generic.TemplateView):
    template_name = 'order/order.html'

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['orders'] = order.models.Order.get_paid_orders()
        return context
