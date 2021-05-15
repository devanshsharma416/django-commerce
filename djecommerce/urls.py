from django.urls import path
from djecommerce import views

app_name = 'djecommerce'

urlpatterns = [
    path('', views.HomeView.as_view(), name = 'home'), 
    path('checkout/', views.CheckoutView.as_view(), name = 'checkout'),
    path('order_summary', views.OrderSummaryView.as_view(), name = 'order_summary'),
    path('product/<slug>/', views.ItemDetailView.as_view(), name = 'product'),
    path('add_to_cart/<slug>/', views.add_to_cart, name = 'add-to-cart'),
    path('add_coupon/', views.AddCoupon.as_view(), name = 'add_coupon'),
    path('remove_from_cart/<slug>/', views.remove_from_cart, name = 'remove-from-cart'),
    path('remove_single_from_cart/<slug>/', views.remove_single_from_cart, name = 'remove-single-from-cart'),
    path('add_to_cart_single/<slug>/', views.add_to_cart_single, name = 'add-to-cart-single'),
    path('payment/<payment_option>/', views.PaymentView.as_view(), name = 'payment'),
    path('request-refund/', views.RequestRefundView.as_view(), name =  'request-refund')
]
