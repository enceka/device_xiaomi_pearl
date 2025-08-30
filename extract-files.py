#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/mediatek',
    'hardware/mediatek/libmtkperf_client',
    'hardware/xiaomi',
    'vendor/xiaomi/pearl'
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
   	'vendor/bin/hw/android.hardware.security.keymint@1.0-service.mitee': blob_fixup()
		.replace_needed('android.system.keystore2-V1-ndk_platform.so', 'android.system.keystore2-V1-ndk.so')
		.replace_needed('android.hardware.security.keymint-V1-ndk_platform.so','android.hardware.security.keymint-V4-ndk.so')
		.replace_needed('android.hardware.security.sharedsecret-V1-ndk_platform.so', 'android.hardware.security.sharedsecret-V1-ndk.so')
		.replace_needed('android.hardware.security.secureclock-V1-ndk_platform.so', 'android.hardware.security.secureclock-V1-ndkso'),

	('vendor/lib64/libmt_mitee@1.3.so',
	'vendor/lib64/libkeymint_support.so'): blob_fixup()
    .replace_needed('android.hardware.security.keymint-V1-ndk_platform.so','android.hardware.security.keymint-V4-ndk.so'),

	'vendor/lib64/libkeystore-engine-wifi-hidl.so': blob_fixup()
    .replace_needed('android.system.keystore2-V1-ndk_platform.so','android.system.keystore2-V1-ndk.so'),

	'vendor/bin/factory': blob_fixup()
    .replace_needed('android.hardware.light-V1-ndk_platform.so', 'android.hardware.light-V1-ndk.so'),
	
	('vendor/bin/hw/android.hardware.gnss-service.mediatek',
	'vendor/lib64/hw/android.hardware.gnss-impl-mediatek.so'): blob_fixup()
    .replace_needed('android.hardware.gnss-V1-ndk_platform.so','android.hardware.gnss-V1-ndk.so'),

	'vendor/bin/hw/android.hardware.lights-service.mediatek': blob_fixup()
    .replace_needed('android.hardware.light-V1-ndk_platform.so','android.hardware.light-V1-ndk.so'),

	'vendor/bin/hw/android.hardware.memtrack-service.mediatek': blob_fixup()
    .replace_needed('android.hardware.memtrack-V1-ndk_platform.so','android.hardware.memtrack-V1-ndk.so'),

	'vendor/bin/hw/android.hardware.vibrator-service.mediatek': blob_fixup()
    .replace_needed('android.hardware.vibrator-V2-ndk_platform.so','android.hardware.vibrator-V2-ndk.so'),

	'vendor/bin/hw/vendor.mediatek.hardware.mtkpower@1.0-service': blob_fixup()
    .replace_needed('android.hardware.power-V2-ndk_platform.so','android.hardware.power-V2-ndk.so'),

	'vendor/bin/hw/vendor.xiaomi.hardware.vibratorfeature.service': blob_fixup()
    .replace_needed('android.hardware.vibrator-V1-ndk_platform.so','android.hardware.vibrator-V1-ndk.so'),

    ('vendor/lib64/mt6895/libcam.hal3a.so',
     'vendor/lib64/mt6895/libcam.hal3a.ctrl.so',
     'vendor/lib64/mt6895/libmtkcam_request_requlator.so'): blob_fixup()
        .add_needed('libprocessgroup_shim.so'),

    ('vendor/lib64/lib3a.ae.pipe.so',
     'vendor/lib64/mt6895/libaaa_toneutil.so',
     'vendor/lib64/mt6895/lib3a.flash.so',
     'vendor/lib64/mt6895/lib3a.sensors.color.so',
     'vendor/lib64/mt6895/lib3a.sensors.flicker.so'): blob_fixup()
        .add_needed('liblog.so'),

    'vendor/lib64/libalhLDC.so': blob_fixup()
        .add_needed('libnativewindow.so')
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),

    'vendor/lib64/libalLDC.so': blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_unlock'),

    ('vendor/lib/libnvram.so',
     'vendor/lib/libsysenv.so',
     'vendor/lib64/libnvram.so',
     'vendor/lib64/libsysenv.so'): blob_fixup()
        .add_needed('libbase_shim.so'),

    ('vendor/lib/libvcodec_oal.so',
     'vendor/lib64/libvcodec_oal.so'): blob_fixup()
        .clear_symbol_version('__aeabi_memcpy')
        .clear_symbol_version('__aeabi_memset')
        .clear_symbol_version('__gnu_Unwind_Find_exidx'),

    ('vendor/lib/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so',
     'vendor/lib64/mt6895/libneuralnetworks_sl_driver_mtk_prebuilt.so'): blob_fixup()
        .clear_symbol_version('AHardwareBuffer_allocate')
        .clear_symbol_version('AHardwareBuffer_release')
        .clear_symbol_version('AHardwareBuffer_createFromHandle')
        .clear_symbol_version('AHardwareBuffer_describe')
        .clear_symbol_version('AHardwareBuffer_getNativeHandle')
        .clear_symbol_version('AHardwareBuffer_lock')
        .clear_symbol_version('AHardwareBuffer_unlock'),

}  # fmt: skip

module = ExtractUtilsModule(
    'pearl',
    'xiaomi',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
