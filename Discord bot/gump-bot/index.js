const { Client, GatewayIntentBits, SlashCommandBuilder, REST, Routes } = require('discord.js');

require('dotenv').config();

const TOKEN=process.env.DISCORD_TOKEN.trim();
const CLIENT_ID=process.env.CLIENT_ID;


const client = new Client({
    intents: [GatewayIntentBits.Guilds]
});

// ----- GUMP LOGIC -----

const GUMP_MINS = 142;
const GUMPS_PER_DAY = [10, 10, 10, 10, 10, 10, 11];

function getGMT0Now() {
    const now = new Date();
    return new Date(now.getTime() + now.getTimezoneOffset() * 60000);
}

function getDayIndex(gmt0) {
    const jsDay = gmt0.getDay();
    return jsDay === 0 ? 6 : jsDay - 1;
}

function gumpsBeforeDay(dayIdx) {
    let total = 0;
    for (let i = 0; i < dayIdx; i++) {
        total += GUMPS_PER_DAY[i];
    }
    return total;
}

function computeGump(gmt0) {
    const dayIdx = getDayIndex(gmt0);
    const isSunday = dayIdx === 6;

    const sod = new Date(gmt0);
    sod.setHours(0, 0, 0, 0);

    const elapsedTodayMins = (gmt0 - sod) / 60000;

    const gumpIdxToday = Math.floor(elapsedTodayMins / GUMP_MINS);
    const withinMins = elapsedTodayMins % GUMP_MINS;
    const progress = withinMins / GUMP_MINS;

    const weekGumpIdx = gumpsBeforeDay(dayIdx) + gumpIdxToday;

    return {
        weekDisplayGump: weekGumpIdx + 1,
        dailyDecimal: `${gumpIdxToday}.${String(Math.floor(progress * 100)).padStart(2, '0')}`,
        minsLeft: Math.round(GUMP_MINS - withinMins),
        isJenny: isSunday && gumpIdxToday >= 10
    };
}

// ----- SLASH COMMAND -----

client.once('ready', () => {
    console.log(`Logged in as ${client.user.tag}`);
});

client.on('interactionCreate', async interaction => {
    if (!interaction.isChatInputCommand()) return;

    if (interaction.commandName === 'time') {
        const gump = computeGump(getGMT0Now());

        await interaction.reply(
            gump.isJenny
                ? '🟠 Current Gump Time: Jenny (Bonus Gump)'
                : `🕒 Current Gump Time: ${gump.dailyDecimal}\nWeek Gump: ${gump.weekDisplayGump}\n${gump.minsLeft} mins remaining`
        );
    }
});

client.login(TOKEN);

console.log("TOKEN EXISTS:", !!TOKEN);
console.log("TOKEN LENGTH:", TOKEN?.length);
console.log("CLIENT_ID:", CLIENT_ID);

client.login(TOKEN);