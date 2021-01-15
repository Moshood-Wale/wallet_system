from django.urls import path
from .views import Register, Login, Wallets, FundWallet, TransactionView, WithdrawWallet


app_name = "wallet_app"

urlpatterns = [
    path('register', Register.as_view()),
    path('login', Login.as_view()),
    path('add_wallet', Wallets.as_view()),
    path('get_wallet', Wallets.as_view()),
    path('fund_wallet', FundWallet.as_view()),
    path('transactions', TransactionView.as_view()),
    path('withdraw', WithdrawWallet.as_view()),
]

