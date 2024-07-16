frappe.ui.form.on('Purchase Order', {
    before_save: function(frm) {
        if (frm.doc.project) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                doctype: 'Project',
                    name: frm.doc.project
                },
                callback: function(r) {
                    if (r.message) {
                        let project = r.message;
                        let assigned_users = project.users;
                        let user = frappe.session.user;
                        let is_assigned = false;

                        assigned_users.forEach(assigned => {
                            if (assigned.user === user) {
                                is_assigned = true;
                            }
                        });

                        if (!is_assigned) {
                            frappe.msgprint({
                                title: __('Invalid Action'),
                                indicator: 'red',
                                message: __('You are not assigned to this project.')
                            });

                            frappe.validated = false;
                        }
                    }
                }
            });
        }
    },

    refresh: function(frm) {
        if (frm.doc.project && frm.doc.docstatus == 0) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Project',
                    name: frm.doc.project
                },
                callback: function(r) {
                    if (r.message) {
                        let project = r.message;

                        limits = {
                            'Werkvoorbereider': frm.doc.custom_werkvoorbereider,
                            'Uitvoerder': frm.doc.custom_uitvoerder,
                            'Projectcoordinator': frm.doc.custom_projectcoordinator,
                            'Projectleider': frm.doc.custom_projectleider,
                            'Bedrijfsleider': frm.doc.custom_bedrijfsleider,
                        }


                        let pending_approval = 'Werkvoorbereider';
                            for (let role in limits) {
                                let limit = limits[role];
                                if (limits[role] >= frm.doc.grand_total) {
                                    pending_approval = role;
                                    break;
                                }

                            }


                        frm.dashboard.add_comment(__("Pending Approval by {0}", [pending_approval]));
                    }
                }
            });
        }
    },

    before_submit: function(frm) {
        // Prevent the form from submitting
        if (frm.doc.project) {
            frappe.call({
                method: 'frappe.client.get',
                args: {
                    doctype: 'Project',
                    name: frm.doc.project,
                },
                callback: function(r) {
                    if (r.message) {
                        let project = r.message;
                        let assigned_users = project.users;
                        let session_user = frappe.session.user;
                        let session_user_role = '';

                        limits = {
                            'Werkvoorbereider': frm.doc.custom_werkvoorbereider,
                            'Uitvoerder': frm.doc.custom_uitvoerder,
                            'Projectcoordinator': frm.doc.custom_projectcoordinator,
                            'Projectleider': frm.doc.custom_projectleider,
                            'Bedrijfsleider': frm.doc.custom_bedrijfsleider,
                        }

                            assigned_users.forEach(assigned => {
                                if (assigned.user == session_user) {
                                    session_user_role = assigned.custom_role;
                                }
                            });

                            if (frm.doc.grand_total > limits[session_user_role]) {

                                frappe.msgprint({
                                    title: __('Invalid Action'),
                                    indicator: 'red',
                                    message: __('Purchase Total exceeds your role limitation. Please Contact your Supervisors'),
                                });

                                frappe.validated = false;
                            }
                    }
                }
            });
        }
    }

});

