cmake_minimum_required(VERSION {{ cookiecutter.minimum_cmake_version }})
project({{ cookiecutter.project_slug }})
{% set dep_pkgs = cookiecutter.dependent_packages.replace(',', ' ').split(' ')|select('ne', '')|list -%}
{% set msgs = cookiecutter.generated_msgs.replace(',', ' ').split(' ')|select('ne', '')|list -%}
{% set srvs = cookiecutter.generated_srvs.replace(',', ' ').split(' ')|select('ne', '')|list -%}
{% set actions = cookiecutter.generated_actions.replace(',', ' ').split(' ')|select('ne', '')|list -%}
{% set dep_msgs = cookiecutter.generated_msgs_depends.replace(',', ' ').split(' ')|select('ne', '')|list %}
find_package(catkin REQUIRED COMPONENTS
{% for pkg in dep_pkgs -%}
{% if pkg|trim|length -%}
  {{ '  ' + pkg }}
{% endif -%}
{% endfor -%}
{%- if msgs|length or srvs|length or actions|length -%}
  {{ '  message_generation' }}
{% endif -%}
)
{% if msgs|length %}
add_message_files(
  DIRECTORY msg
  FILES
{% for msg in msgs -%}
{% set root_name = msg.partition('.')[0]|trim -%}
{% if root_name|length -%}
    {{ '    ' + root_name }}.msg
{% endif -%}
{% endfor -%}
)
{% endif -%}

{% if srvs|length %}
add_service_files(
  DIRECTORY srv
  FILES
{% for srv in srvs -%}
{% set root_name = srv.partition('.')[0]|trim -%}
{% if root_name|length -%}
    {{ '    ' + root_name }}.srv
{% endif -%}
{% endfor -%}
)
{% endif -%}

{% if actions|length %}
add_action_files(
  DIRECTORY action
  FILES
{% for action in actions -%}
{% set root_name = action.partition('.')[0]|trim -%}
{% if root_name|length -%}
    {{ '    ' + root_name }}.action
{% endif -%}
{% endfor -%}
)
{% endif %}
catkin_python_setup()

{% if msgs|length + srvs|length + actions|length -%}
{% if dep_msgs|length -%}
generate_messages(
  DEPENDENCIES
{% for msg in dep_msgs -%}
{% if msg|trim|length -%}
    {{ '    ' + msg }}
{% endif -%}
{% endfor -%}
)
{% else -%}
generate_messages()
{% endif %}
{% endif -%}
catkin_package()

catkin_install_python(PROGRAMS
  nodes/{{ cookiecutter.project_slug }}_node.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
