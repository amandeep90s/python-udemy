users: list[dict[str, int | str]] = [
    {"id": 1, "total": 500, "coupon": "COUPON1"},
    {"id": 2, "total": 200, "coupon": "COUPON2"},
    {"id": 3, "total": 100, "coupon": "COUPON3"},
]

discounts: dict[str, tuple[float, int]] = {
    "COUPON1": (0.1, 0),
    "COUPON2": (0.2, 0),
    "COUPON3": (0, 10),
}

for user in users:
    coupon = str(user["coupon"])
    total = int(user["total"])
    percent, fixed = discounts.get(coupon, (0, 0))
    discount = total * percent + fixed
    print(f"User {user['id']}: {coupon} discount: {discount}")