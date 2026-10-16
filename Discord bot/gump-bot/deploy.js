const { REST, Routes, SlashCommandBuilder } = require('discord.js');

require('dotenv').config();

const TOKEN=process.env.DISCORD_TOKEN.trim();
const CLIENT_ID=process.env.CLIENT_ID;


const commands = [
    new SlashCommandBuilder()
        .setName('time')
        .setDescription('Shows the current Gump time')
        .toJSON()
];

const rest = new REST({ version: '10' }).setToken(TOKEN);

(async () => {
    try {
        await rest.put(
            Routes.applicationCommands(CLIENT_ID),
            { body: commands },
        );

        console.log('Slash command registered.');
    } catch (error) {
        console.error(error);
    }
})();