from PyroUbot import *
import asyncio

__MODULE__ = "ᴇᴍᴏᴊɪ"
__HELP__ = """
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴇᴍᴏᴊɪ ⦫</b>

ᚗ <code>{0}emoji</code> query emojiprem
⊶ untuk merubah emoji pada tampilan tertentu

query:
    ⊶ <code>{0}pong</code>
    ⊶ <code>{0}owner</code>
    ⊶ <code>{0}ubot</code>
    ⊶ <code>{0}gcast</code>
    ⊶ <code>{0}sukses</code>
    ⊶ <code>{0}gagal</code>
    ⊶ <code>{0}proses</code>
    ⊶ <code>{0}group</code>
    ⊶ <code>{0}catatan</code>
    ⊶ <code>{0}afk</code>
    ⊶ <code>{0}waktu</code>
    ⊶ <code>{0}alasan</code></blockquote>
"""


@PY.UBOT("creat")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply(
            f"{message.text} [group/channel] [name/titlee]")
    group_type = message.command[1]
    split = message.command[2:]
    group_name = " ".join(split)
    xd = await message.reply("memproꜱeꜱ...")
    desc = "Welcome To My " + ("Group" if group_type == "gc" else "Channel")
    if group_type == "group":
        _id = await client.create_supergroup(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram grup: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )
    elif group_type == "channel":
        _id = await client.create_channel(group_name, desc)
        link = await client.get_chat(_id.id)
        await xd.edit(
            f"berhaꜱil membuat telegram channel: [{group_name}]({link.invite_link})",
            disable_web_page_preview=True,
        )


@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs}memproses...", quote=True)
    if len(message.command) < 2:
        return await Tm.edit(f"{ggl}{message.text} [simbol]")
    else:
        ub_prefix = []
        for prefix in message.command[1:]:
            if prefix.lower() == "none":
                ub_prefix.append("")
            else:
                ub_prefix.append(prefix)
        try:
            client.set_prefix(message.from_user.id, ub_prefix)
            await set_pref(message.from_user.id, ub_prefix)
            parsed_prefix = " ".join(f"{prefix}" for prefix in ub_prefix)
            return await Tm.edit(f"<blockquote><b>{brhsl}prefix telah diubah ke: {parsed_prefix}</blockquote></b>\n\n<blockquote><b>ᴀᴡᴀs ᴋᴀʟᴏ ʙᴜᴀᴛ ᴘʀᴇғɪx ᴊᴀɴɢᴀɴ sᴀᴍᴘᴇ ʟᴜᴘᴀ ᴘʀᴇғɪx ʏᴀɴɢ ʟᴜ ɢᴀɴᴛɪ ᴀᴘᴀ !!</blockquote></b>")
        except Exception as error:
            return await Tm.edit(str(error))


@PY.BOT("resetprefix")
async def _(client, message):
    listId = []
    msg = await message.reply("Sedang memproses...")
    for x in ubot._ubot:
        listId.append(x.me.id)

    if message.from_user.id  not in listId:
        return await msg.edit("anda belum memasang userbot")
    else:
        ubot.set_prefix(message.from_user.id, ["."])
        await set_pref(message.from_user.id, ["."])
        return await msg.edit("prefix berhasil diriset menjadi . (titik.")



@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    msg_afk = (
        f"<blockquote><b>{tion}sedang afk\n{ktrng}alasan: {reason}</blockquote></b>"
        if reason
        else f"{tion}sedang afk"
      )
    await set_vars(client.me.id, "AFK", db_afk)
    return await message.reply(msg_afk)



@PY.NO_CMD_UBOT("AFK", ubot)
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        rpk = f"[{message.from_user.first_name} {message.from_user.last_name or ''}](tg://user?id={message.from_user.id})"
        afk_text = (
            f"<blockquote><b>{tion}sedang afk\n{mng}waktu: {afk_runtime}\n{ktrng}alasan: {afk_reason}</blockquote></b>"
            if afk_reason
            else f"""
<blockquote><b>hello {rpk}
tuan saya sedang afk selama : {afk_runtime}
mohon tunggu beberapa waktu</blockquote></b>
"""
        )
        msg = await message.reply(afk_text)
        await asyncio.sleep(1)
        await msg.delete()


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    tion = await EMO.AEFKA(client)
    ktrng = await EMO.ALASAN(client)
    mng = await EMO.WAKTU(client)
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        afk_text = f"<blockquote><b>{tion}kembali online\n{mng}afk selama: {afk_runtime}</blockquote></b>"
        await message.reply(afk_text)
        return await remove_vars(client.me.id, "AFK")


@PY.UBOT("emoji")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    try:
        msg = await message.reply(f"{prs}memproses...", quote=True)

        query_mapping = {
            "pong": "EMOJI_PING",
            "owner": "EMOJI_MENTION",
            "ubot": "EMOJI_USERBOT",
            "proses": "EMOJI_PROSES",
            "gcast": "EMOJI_BROADCAST",
            "sukses": "EMOJI_BERHASIL",
            "gagal": "EMOJI_GAGAL",
            "catatan": "EMOJI_KETERANGAN",
            "group": "EMOJI_GROUP",
            "menunggu": "EMOJI_MENUNGGU",
            "alasan": "EMOJI_ALASAN",
            "waktu": "EMOJI_WAKTU",
            "afk": "EMOJI_AFKA",
        }

        parts = message.text.split(maxsplit=3)
        if len(parts) < 3:
            return await msg.edit(
                f"{ggl}format salah!\n\n"
                f"Contoh:\n"
                f"- `.emoji set proses ⏳` (emoji biasa)\n"
                f"- reply emoji premium → `.emoji set proses`"
            )

        action, mapping = parts[1].lower(), parts[2].lower()
        value = parts[3] if len(parts) > 3 else None

        if action != "set":
            return await msg.edit(f"{ggl}gunakan format: `.emoji set [mapping] [emoji]`")

        if mapping not in query_mapping:
            return await msg.edit(f"{ggl}mapping `{mapping}` tidak ditemukan")

        query_var = query_mapping[mapping]

        # Case 1 → reply premium emoji
        if message.reply_to_message and message.reply_to_message.entities:
            for entity in message.reply_to_message.entities:
                if entity.custom_emoji_id:
                    emoji_id = entity.custom_emoji_id
                    await set_vars(client.me.id, query_var, emoji_id)
                    try:
                        return await msg.edit(
                            f"{brhsl}emoji premium berhasil di set ke: "
                            f"<emoji id={emoji_id}>⭐️</emoji>\n"
                            f"🆔 ID: <code>{emoji_id}</code>"
                        )
                    except Exception:
                        return await message.reply(
                            f"{brhsl}emoji premium berhasil di set ke: "
                            f"<emoji id={emoji_id}>⭐️</emoji>\n"
                            f"🆔 ID: <code>{emoji_id}</code>"
                        )

        # Case 2 → argumen emoji biasa
        if value:
            char = value[0]
            unicode_code = f"U+{ord(char):X}"
            await set_vars(client.me.id, query_var, char)
            try:
                return await msg.edit(
                    f"{brhsl}emoji biasa berhasil di set ke: {char}\n"
                    f"🆔 Unicode: <code>{unicode_code}</code>"
                )
            except Exception:
                return await message.reply(
                    f"{brhsl}emoji biasa berhasil di set ke: {char}\n"
                    f"🆔 Unicode: <code>{unicode_code}</code>"
                )

        return await msg.edit(f"{ggl}tidak menemukan emoji untuk diset")

    except Exception as error:
        await msg.edit(f"{ggl}{str(error)}")

