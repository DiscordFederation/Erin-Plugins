from roles import PersistRoles

plugin_data = {
    "name": "Erin Role Plugins",
    "database": "mongodb"
}


def setup(bot):
    bot.add_cog(PersistRoles(bot))
