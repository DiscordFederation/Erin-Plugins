from plugins.maintainance.server_status import ServerStatus

plugin_data = {
    "name": "Erin Maintenance Plugin"
}


def setup(bot):
    bot.add_cog(ServerStatus(bot))
