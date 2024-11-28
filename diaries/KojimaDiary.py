from diaries.AbstractDiary import AbstractDiary

class NagataniDiary(AbstractDiary):
    def get_date(self):
        return "2024-11-28"
    
    def get_summary(self):
        return """今日は第9回のグループワークでGitHubの勉強をしました。
        まだ触り始めだらよくわからないこともあるけど、チームと協力して進めていけるように頑張りたい。
        マージ、プル、プッシュなどわからないことも多いが慣れていければ良いと考える。"""

    def get_author(self):
        return "kojima"