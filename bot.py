import discord
import config
from discord.ext import commands

# 봇 설정
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

# 금지어 목록
banned_words = ["민규", "민큐", "혜강", "해강", "무현", "부엉이", "노무현", "두현", "전두환", "노짱", "ghggc", "밀지마라", "colpop, 콜팝"
                , "뮌규", "밍규", "뮝규", "믱규", "므잉큐", "믱큐", "므잉규", "pmg", "성재", "믠큐", "믱큐", "민q", "민Q", "뮝Q", "뮝q", 
                "뮝Q", "뮝q", "민1규", "민1큐", "믱1규", "믱1큐", "밍1규", "밍1큐", "믱", "믠", "뮌", "뮝", "묑", "므잉", "므인", "므읜",
                "무잉", "고혜", "때려", "ming", "고1", "혜1", "해1", "kolpop", "kolpap", "colpap", "예강", "꼴밥", "꼴팝", "콜빱", "콜밥"]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    if message.author.bot:
        return
     
    # 관리자 예외 처리
    if message.author.guild_permissions.administrator:
        await bot.process_commands(message)
        return

    # 메시지에 금지어가 있는지 검사
    if any(bad_word in message.content for bad_word in banned_words):
        await message.delete()
        await message.channel.send(f"{message.author.mention} 금지어가 감지되어 삭제되었습니다.", delete_after=5)
        try:
            # 10분 타임아웃 설정
            duration = datetime.timedelta(minutes=10)
            await message.author.timeout(datetime.datetime.utcnow() + duration, reason="금지어 사용")
        except Exception as e:
            print("타임아웃 실패:", e)

    await bot.process_commands(message)

bot.run(config.DISCORD_BOT_TOKEN)

