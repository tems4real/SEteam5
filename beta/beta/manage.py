#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "beta.settings"
    )
    from django.contrib.auth.models import Permission, User
    from django.shortcuts import get_object_or_404

    def user_gains_perms(request, user_id):
        user = get_list_or_404(User, pk=user_id)
        user.has_perm('myapp.change_bar')
        
        permission = Permission.objects.get_by_natural_key(codename= 'change_bar')
        user.user_permissions.add(permission)
        user.has_perm('myapp.change_bar')
        
        user = get_object_or_404(User, pk=user_id)
        
        user.has_perm('myapp.change_bar') 

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
