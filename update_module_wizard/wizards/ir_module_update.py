from odoo import fields, models


class IrModuleUpdate(models.TransientModel):
    _name = 'ir.module.update'
    _description = 'Module Update'

    module_id = fields.Many2one(
        comodel_name='ir.module.module',
        required=True,
        domain="[('state', 'in', ['uninstalled', 'installed'])]",
    )
    latest_version = fields.Char(
        related='module_id.latest_version',
    )

    def run(self):
        self.ensure_one()

        if self.module_id.state == 'uninstalled':
            return self.module_id.button_immediate_install()

        return self.module_id.button_immediate_upgrade()
