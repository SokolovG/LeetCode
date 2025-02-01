from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        s = set()
        for e in emails:
            name, dom = e.split('@')
            name = name.split('+')[0]
            name = name.replace('.', '')
            s.add(f'{name}@{dom}')

        return len(s)