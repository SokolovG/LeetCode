class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:  # Пока двухзначное
            print(f"\nТекущее num: {num}")

            cur = num  # Сохраняем текущее число в cur.
            new_num = 0  # Создаем переменную для суммы цифр.

            while cur:  # Пока cur не станет 0.
                cur, d = divmod(cur, 10)  # Делим cur на 10.
                print(f"cur: {cur}, d: {d}")
                new_num += d  # Добавляем остаток к сумме.
                print(f"new_num: {new_num}")

            num = new_num  # Обновляем num новой суммой.

        return num


s = Solution()
