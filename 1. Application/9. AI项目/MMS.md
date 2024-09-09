# 简介

> 体验地址：https://huggingface.co/spaces/mms-meta/MMS

> 项目地址：https://github.com/facebookresearch/fairseq/tree/main/examples/mms

# 测试用例
由于不支持普通话，只支持闽南语、客家话，所以测试英语

|||内容|单词数|出错数量|生成时长|
|-|-|-|-|-|-|
|测试一|原文|I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation.|27|
|测试一|输出|I am happy to join with you today in what will go down in history as the greatest demonstration for freedom in the history of our nation.|27|0|5秒|

|||内容|单词数|出错数量|生成时长|
|-|-|-|-|-|-|
|测试二|原文|but one hundred years later the negro still is not free one hundred years later the life of the negro is still sadly crippled by the manacles of segregation and the chains of discrimination one hundred years later the negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity one hundred years later the negro is still languished in the corners of american society and finds himself an exile in his own land and so we have come here today to dramatize a shameful condition|93|||
|测试二|输出|but one hundred years later the negro still is not free one hundred years later the life of the negro is still sadly crippled by the manacles of segregation and the chains of discrimination one hundred years later the negro lives on a lonely island of poverty in the midst of a vast ocean of material prosperity one hundred years later the negro is still languished in the corners of american society and finds himself an exile in his own land and so we have come here today to dramatize a shameful condition|93|0|9秒|

|||内容|单词数|出错数量|生成时长|
|-|-|-|-|-|-|
|测试三|原文|We have also come to this hallowed spot to remind America of the fierce urgency of Now. This is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism. Now is the time to make real the promises of democracy. Now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice. Now is the time to lift our nation from the quicksands of racial injustice to the solid rock of brotherhood. Now is the time to make justice a reality for all of God's children.|103|
|测试三|输出|we have also come to this hallowed spot to remind america of the fierce urgency of now this is no time to engage in the luxury of cooling off or to take the tranquilizing drug of gradualism now is the time to make real the promises of democracy now is the time to rise from the dark and desolate valley of segregation to the sunlit path of racial justice now is the time to lift our nation from the quicksand of racial injustice to the solid rock of brotherhood now is the time to make justice a reality for all of god backslash as children|105|1|9秒|


|||内容|单词数|出错数量|生成时长|
|-|-|-|-|-|-|
|测试四|原文|It would be fatal for the nation to overlook the urgency of the moment. This sweltering summer of the Negro's legitimate discontent will not pass until there is an invigorating autumn of freedom and equality. Nineteen sixty-three is not an end, but a beginning. And those who hope that the Negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual. And there will be neither rest nor tranquility in America until the Negro is granted his citizenship rights. The whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges.|112|||
|测试四|输出|it would be fatal for the nation to overlook the urgency of the moment this sweltering summer of the negro backslash as legitimate discontent will not pass until there is an invigorating autumn of freedom and equality nineteen sixty-three is not an end but a beginning and those who hope that the negro needed to blow off steam and will now be content will have a rude awakening if the nation returns to business as usual and there will be neither rest nor tranquility in america until the negro is granted his citizenship rights the whirlwinds of revolt will continue to shake the foundations of our nation until the bright day of justice emerges|114|1|10秒|

|||内容|单词数|出错数量|生成时长|
|-|-|-|-|-|-|
|测试五|原文|The marvelous new militancy which has engulfed the Negro community must not lead us to a distrust of all white people, for many of our white brothers, as evidenced by their presence here today, have come to realize that their destiny is tied up with our destiny. And they have come to realize that their freedom is inextricably bound to our freedom.|62|
|测试五|输出|the marvelous new militancy which has engulfed the negro community must not lead us to a distrust of all white people for many of our white brothers as evidenced by their presence here today have come to realize that their destiny is tied up with our destiny and they have come to realize that their freedom is inextricably bound to our freedom|62|0|7秒|

