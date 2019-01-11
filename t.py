
def T_factory(env):
    def get_T(prefix):
        def T(template_name, **kwargs):
            template_name = prefix + '/' + template_name
            template = env.get_template(template_name)
            kwargs['T'] = T
            return template.render(**kwargs)
        return T
    return get_T