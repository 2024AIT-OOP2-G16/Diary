from diaries.AbstractDiary import AbstractDiary

class hanadaDiary(AbstractDiary):

    def get_date(self):
        return "2024-11-28"

    def get_summary(self):
        return  """今日は、朝5時半に起きて終わっていないオブジェクト演習の課題と物理実験の課題をやっていました。
村中先生によるレポートの添削を終えたのであとはレポート用紙に写すだけです。
この後頑張らないといけないと感じました。"""

    def get_author(self):
        return "花田歩夢"