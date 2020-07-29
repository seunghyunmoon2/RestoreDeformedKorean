# -*- coding: utf-8 -*-

!pip install KoSpacing

from hangul_utils import Preprocessor
p = Preprocessor()
p.normalize("부들부들부들부들 내가 작간데 화가낰ㅋㅋㅋㅋ")
#"부들부들 내가 작가인데 화가나ㅋㅋㅋ"

from hangul_utils import normalize
normalize("부들부들부들부들 내가 작간데 화가낰ㅋㅋㅋㅋ")
#"부들부들 내가 작가인데 화가나ㅋㅋㅋ"