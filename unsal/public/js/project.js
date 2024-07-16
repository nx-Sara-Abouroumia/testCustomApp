frappe.ui.form.on('Project', {
    before_save: function(frm) {
        const required_roles = ['Projectleider', 'Uitvoerder', 'Werkvoorbereider', 'Bedrijfsleider'];
        let roles_filled = {};

        required_roles.forEach(role => {
            roles_filled[role] = false;
        });

        frm.doc.users.forEach(user => {
            if (required_roles.includes(user.custom_role)) {
                roles_filled[user.custom_role] = true;
            }
        });

        let missing_roles = required_roles.filter(role => !roles_filled[role]);

        if (missing_roles.length > 0) {
            let formatted_roles = missing_roles.map(role => `<div style="color: #8B0000;">${role}</div>`).join('');

            frappe.msgprint({
                title: __('Invalid Action'),
                indicator: 'red',
                message: __('Please assign at least one user to the following roles: {0}', [formatted_roles]),
            });

            frappe.validated = false;
        }
    }
});
