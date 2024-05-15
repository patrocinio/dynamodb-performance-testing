import serverless_sdk
sdk = serverless_sdk.SDK(
    org_id='patrocinio',
    application_name='dynamodb-performance-testing-dev',
    app_uid='d1p1rQcjDbs1gh34JV',
    org_uid='6b1bbb85-13e3-438d-8975-ca78ba25fdb6',
    deployment_uid='cf395246-1d70-4cc2-be2e-138762913209',
    service_name='dynamodb-performance-testing',
    should_log_meta=True,
    should_compress_logs=True,
    disable_aws_spans=False,
    disable_http_spans=False,
    stage_name='dev',
    plugin_version='7.2.3',
    disable_frameworks_instrumentation=False,
    serverless_platform_stage='prod'
)
handler_wrapper_kwargs = {'function_name': 'dynamodb-performance-testing-dev-transactWriteItem5Fail', 'timeout': 6}
try:
    user_handler = serverless_sdk.get_user_handler('transact_write.handler')
    handler = sdk.handler(user_handler, **handler_wrapper_kwargs)
except Exception as error:
    e = error
    def error_handler(event, context):
        raise e
    handler = sdk.handler(error_handler, **handler_wrapper_kwargs)
