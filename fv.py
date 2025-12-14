# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# FutureVisions Obfuscator - v1.7.0


import ast
import base64
import hashlib
import marshal
import os
import platform
import random
import re
import shutil
import sys
import time
import traceback
import zlib
from datetime import datetime
import uuid
import fade
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

blacklist_usernames = ['dekker', 'WDAGUtilityAccount', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'Bruno', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg', 'stephpie']
blacklist_hostnames = ['DESKTOP-EIWAI7B', '0CC47AC83802', 'BEE7370C-8C0C-4', 'DESKTOP-ET51AJO', '965543', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42', 'test']
blacklist_hwids = ['671BC5F7-4B0F-FF43-B923-8B1645581DC8', '7AB5C494-39F5-4941-9163-47F54D6D5016', '03DE0294-0480-05DE-1A06-350700080009', '11111111-2222-3333-4444-555555555555', '6F3CA5EC-BEC9-4A4D-8274-11168F640058', 'ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548', '4C4C4544-0050-3710-8058-CAC04F59344A', '00000000-0000-0000-0000-AC1F6BD04972', '00000000-0000-0000-0000-000000000000', '5BD24D56-789F-8468-7CDC-CAA7222CC121', '49434D53-0200-9065-2500-65902500E439', '49434D53-0200-9036-2500-36902500F022', '777D84B3-88D1-451C-93E4-D235177420A7', '49434D53-0200-9036-2500-369025000C65', 'B1112042-52E8-E25B-3655-6A4F54155DBF', '00000000-0000-0000-0000-AC1F6BD048FE', 'EB16924B-FB6D-4FA1-8666-17B91F62FB37', 'A15A930C-8251-9645-AF63-E45AD728C20C', '67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3', 'C7D23342-A5D4-68A1-59AC-CF40F735B363', '63203342-0EB0-AA1A-4DF5-3FB37DBB0670', '44B94D56-65AB-DC02-86A0-98143A7423BF', '6608003F-ECE4-494E-B07E-1C4615D1D93C', 'D9142042-8F51-5EFF-D5F8-EE9AE3D1602A', '49434D53-0200-9036-2500-369025003AF0', '8B4E8278-525C-7343-B825-280AEBCD3BCB', '4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27', '79AF5279-16CF-4094-9758-F88A616D81B4', 'FF577B79-782E-0A4D-8568-B35A9B7EB76B', '08C1E400-3C56-11EA-8000-3CECEF43FEDE', '6ECEAF72-3548-476C-BD8D-73134A9182C8', '49434D53-0200-9036-2500-369025003865', '119602E8-92F9-BD4B-8979-DA682276D385', '12204D56-28C0-AB03-51B7-44A8B7525250', '63FA3342-31C7-4E8E-8089-DAFF6CE5E967', '365B4000-3B25-11EA-8000-3CECEF44010C', 'D8C30328-1B06-4611-8E3C-E433F4F9794E', '00000000-0000-0000-0000-50E5493391EF', '00000000-0000-0000-0000-AC1F6BD04D98', '4CB82042-BA8F-1748-C941-363C391CA7F3', 'B6464A2B-92C7-4B95-A2D0-E5410081B812', 'BB233342-2E01-718F-D4A1-E7F69D026428', '9921DE3A-5C1A-DF11-9078-563412000026', 'CC5B3F62-2A04-4D2E-A46C-AA41B7050712', '00000000-0000-0000-0000-AC1F6BD04986', 'C249957A-AA08-4B21-933F-9271BEC63C85', 'BE784D56-81F5-2C8D-9D4B-5AB56F05D86E', 'ACA69200-3C4C-11EA-8000-3CECEF4401AA', '3F284CA4-8BDF-489B-A273-41B44D668F6D', 'BB64E044-87BA-C847-BC0A-C797D1A16A50', '2E6FB594-9D55-4424-8E74-CE25A25E36B0', '42A82042-3F13-512F-5E3D-6BF4FFFD8518', '38AB3342-66B0-7175-0B23-F390B3728B78', '48941AE9-D52F-11DF-BBDA-503734826431', '032E02B4-0499-05C3-0806-3C0700080009', 'DD9C3342-FB80-9A31-EB04-5794E5AE2B4C', 'E08DE9AA-C704-4261-B32D-57B2A3993518', '07E42E42-F43D-3E1C-1C6B-9C7AC120F3B9', '88DC3342-12E6-7D62-B0AE-C80E578E7B07', '5E3E7FE0-2636-4CB7-84F5-8D2650FFEC0E', '96BB3342-6335-0FA8-BA29-E1BA5D8FEFBE', '0934E336-72E4-4E6A-B3E5-383BD8E938C3', '12EE3342-87A2-32DE-A390-4C2DA4D512E9', '38813342-D7D0-DFC8-C56F-7FC9DFE5C972', '8DA62042-8B59-B4E3-D232-38B29A10964A', '3A9F3342-D1F2-DF37-68AE-C10F60BFB462', 'F5744000-3C78-11EA-8000-3CECEF43FEFE', 'FA8C2042-205D-13B0-FCB5-C5CC55577A35', 'C6B32042-4EC3-6FDF-C725-6F63914DA7C7', 'FCE23342-91F1-EAFC-BA97-5AAE4509E173', 'CF1BE00F-4AAF-455E-8DCD-B5B09B6BFA8F', '050C3342-FADD-AEDF-EF24-C6454E1A73C9', '4DC32042-E601-F329-21C1-03F27564FD6C', 'DEAEB8CE-A573-9F48-BD40-62ED6C223F20', '05790C00-3B21-11EA-8000-3CECEF4400D0', '5EBD2E42-1DB8-78A6-0EC3-031B661D5C57', '9C6D1742-046D-BC94-ED09-C36F70CC9A91', '907A2A79-7116-4CB6-9FA5-E5A58C4587CD', 'A9C83342-4800-0578-1EE8-BA26D2A678D2', 'D7382042-00A0-A6F0-1E51-FD1BBF06CD71', '1D4D3342-D6C4-710C-98A3-9CC6571234D5', 'CE352E42-9339-8484-293A-BD50CDC639A5', '60C83342-0A97-928D-7316-5F1080A78E72', '02AD9898-FA37-11EB-AC55-1D0C0A67EA8A', 'DBCC3514-FA57-477D-9D1F-1CAF4CC92D0F', 'FED63342-E0D6-C669-D53F-253D696D74DA', '2DD1B176-C043-49A4-830F-C623FFB88F3C', '4729AEB0-FC07-11E3-9673-CE39E79C8A00', '84FE3342-6C67-5FC6-5639-9B3CA3D775A1', 'DBC22E42-59F7-1329-D9F2-E78A2EE5BD0D', 'CEFC836C-8CB1-45A6-ADD7-209085EE2A57', 'A7721742-BE24-8A1C-B859-D7F8251A83D3', '3F3C58D1-B4F2-4019-B2A2-2A500E96AF2E', 'D2DC3342-396C-6737-A8F6-0C6673C1DE08', 'EADD1742-4807-00A0-F92E-CCD933E9D8C1', 'AF1B2042-4B90-0000-A4E4-632A1C8C7EB1', 'FE455D1A-BE27-4BA4-96C8-967A6D3A9661', '921E2042-70D3-F9F1-8CBD-B398A21F89C6']
blacklist_programs = ['cheatengine', 'cheat engine', 'x32dbg', 'x64dbg', 'ollydbg', 'windbg', 'ida', 'ida64', 'ghidra', 'radare2', 'radare', 'dbg', 'immunitydbg', 'dnspy', 'softice', 'edb', 'debugger', 'visual studio debugger', 'lldb', 'gdb', 'valgrind', 'hex-rays', 'disassembler', 'tracer', 'debugview', 'procdump', 'strace', 'ltrace', 'drmemory', 'decompiler', 'hopper', 'binary ninja', 'bochs', 'vdb', 'frida', 'api monitor', 'process hacker', 'sysinternals', 'procexp', 'process explorer', 'monitor tool', 'vmmap', 'xperf', 'perfview', 'py-spy', 'strace-log']


def _rand_ident(prefix: str = "_16z_", length: int = 12) -> str:
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return prefix + "".join(random.choice(alphabet) for _ in range(length))


class VariableCollector(ast.NodeVisitor):
    """
    Tìm tất cả các biến được gán trong code
    """
    def __init__(self):
        self.assigned_vars = set()
        self.global_vars = set()
        self.arg_names = set()

    def visit_Global(self, node):
        self.global_vars.update(node.names)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            self.assigned_vars.add(node.id)
        self.generic_visit(node)

    def visit_arg(self, node):
        self.arg_names.add(node.arg)
        self.assigned_vars.add(node.arg)
        self.generic_visit(node)


class VariableRenamer(ast.NodeTransformer):
    """
    sửa tên biến local
    """
    def __init__(self, assigned_vars, arg_names):
        self.assigned_vars = set(assigned_vars)
        self.arg_names = set(arg_names)
        self.var_map = {}

        for a in self.arg_names:
            self.assigned_vars.discard(a)

    def _obf_name(self, original: str) -> str:
        return f"var_{hashlib.shake_128(original.encode()).hexdigest(8)}"

    def visit_Name(self, node):
        if node.id in self.assigned_vars:
            if node.id not in self.var_map:
                self.var_map[node.id] = self._obf_name(node.id)
            node.id = self.var_map[node.id]
        return node

    def visit_arg(self, node):
        return node


class ControlFlowFlattener(ast.NodeTransformer):
    """
    biến tất cả các hàm thành một while+if state machine
    """

    COMPLEX_NODES = (
        ast.Return,
        ast.Yield,
        ast.YieldFrom,
        ast.AsyncFunctionDef,
        ast.Try,
        ast.With,
        ast.Break,
        ast.Continue,
    )

    def visit_FunctionDef(self, node: ast.FunctionDef):
        # Kiểm tra nonlocal TRƯỚC khi xử lý để tránh lỗi
        if any(isinstance(n, ast.Nonlocal) for n in ast.walk(node)):
            self.generic_visit(node)
            return node
        
        self.generic_visit(node)

        if any(isinstance(n, self.COMPLEX_NODES) for n in ast.walk(node)):
            return node

        original_body = list(node.body)
        if not original_body:
            return node

        assigned_in_func = set()
        arg_names = set()
        globals_in_func = set()
        nonlocals_in_func = set()

        for n in ast.walk(node):
            if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store):
                assigned_in_func.add(n.id)
            elif isinstance(n, ast.arg):
                arg_names.add(n.arg)
            elif isinstance(n, ast.Global):
                globals_in_func.update(n.names)
            elif isinstance(n, ast.Nonlocal):
                nonlocals_in_func.update(n.names)

        assigned_locals = {
            name
            for name in assigned_in_func
            if name not in globals_in_func
            and name not in nonlocals_in_func
            and name not in arg_names
        }

        initializers = []
        for name in sorted(assigned_locals):
            if name.startswith("__") and name.endswith("__"):
                continue
            init = ast.Assign(
                targets=[ast.Name(id=name, ctx=ast.Store())],
                value=ast.Constant(value=None)
            )
            initializers.append(init)

        state_var = f"state_{random.randint(1000, 9999)}"

        new_body = [
            ast.Assign(
                targets=[ast.Name(id=state_var, ctx=ast.Store())],
                value=ast.Constant(value=0)
            )
        ]

        new_body.extend(initializers)

        while_body = []
        flattenable_statements = []
        flattenable_indices = []
        for i, stmt in enumerate(original_body):
            if isinstance(stmt, (ast.Try, ast.With, ast.AsyncFunctionDef, ast.FunctionDef)):
                continue
            if any(isinstance(n, (ast.Try, ast.With, ast.Break, ast.Continue)) for n in ast.walk(stmt)):
                continue
            flattenable_statements.append(stmt)
            flattenable_indices.append(i)
        
        if not flattenable_statements:
            return node
        
        total_statements = len(flattenable_statements)
        junk_count = int(total_statements * 0.75)  
        junk_indices = set(random.sample(range(total_statements), min(junk_count, total_statements)))
        
        original_index_map = {idx: orig_idx for idx, orig_idx in enumerate(flattenable_indices)}
        
        for i, stmt in enumerate(flattenable_statements):
            original_idx = flattenable_indices[i]
            dispatch_if = ast.If(
                test=ast.Compare(
                    left=ast.Name(id=state_var, ctx=ast.Load()),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(value=original_idx)]
                ),
                body=[
                    stmt,
                    ast.AugAssign(
                        target=ast.Name(id=state_var, ctx=ast.Store()),
                        op=ast.Add(),
                        value=ast.Constant(value=1)
                    )
                ],
                orelse=[]
            )
            while_body.append(dispatch_if)

            if i in junk_indices:
                opaque_if = ast.If(
                    test=ast.Compare(
                        left=ast.BinOp(
                            left=ast.Constant(123),
                            op=ast.Mult(),
                            right=ast.Constant(456),
                        ),
                        ops=[ast.Eq()],
                        comparators=[ast.Constant(789)],  # luôn luôn false vì 123*456 = 56088 :V
                    ),
                    body=[ast.Expr(value=ast.Constant(value=None))],
                    orelse=[]
                )
                while_body.append(opaque_if)

        max_state = max(flattenable_indices) + 1 if flattenable_indices else 0
        
        new_body.append(
            ast.While(
                test=ast.Compare(
                    left=ast.Name(id=state_var, ctx=ast.Load()),
                    ops=[ast.Lt()],
                    comparators=[ast.Constant(value=max_state)]
                ),
                body=while_body,
                orelse=[]
            )
        )

        node.body = new_body
        return node


class ConstantObfuscator(ast.NodeTransformer):
    """
    làm 1 phép tính trở nên phức tạp..
    """
    def visit_Constant(self, node: ast.Constant):
        if isinstance(node.value, int):
            if node.value == 0:
                return ast.BinOp(left=ast.Constant(1), op=ast.Sub(), right=ast.Constant(1))
            elif node.value == 1:
                return ast.BinOp(left=ast.Constant(2), op=ast.Sub(), right=ast.Constant(1))
            elif node.value > 1 and node.value < 100:
                a = random.randint(1, node.value - 1) if node.value > 1 else 0
                b = node.value - a
                return ast.BinOp(left=ast.Constant(a), op=ast.Add(), right=ast.Constant(b))
            elif node.value < 0:
                return ast.UnaryOp(op=ast.USub(), operand=ast.Constant(abs(node.value)))
        elif isinstance(node.value, bool):
            if node.value:
                return ast.Compare(left=ast.Constant(1), ops=[ast.Eq()], comparators=[ast.Constant(1)])
            else:
                return ast.Compare(left=ast.Constant(1), ops=[ast.Eq()], comparators=[ast.Constant(0)])
        elif node.value is None:
            return ast.Call(func=ast.Name(id='type', ctx=ast.Load()), args=[ast.Constant(None)], keywords=[])
        return node


class DeadCodeInjector(ast.NodeTransformer):
    """
    Thêm dead code vào các hàm
    """
    def visit_FunctionDef(self, node: ast.FunctionDef):
        self.generic_visit(node)
        
        if any(isinstance(n, (ast.Try, ast.With, ast.AsyncFunctionDef)) for n in ast.walk(node)):
            return node
        
        if not node.body:
            return node
        
        dead_vars = []
        for _ in range(random.randint(1, 3)):
            var_name = _rand_ident("_dead_", 8)
            dead_vars.append(ast.Assign(
                targets=[ast.Name(id=var_name, ctx=ast.Store())],
                value=ast.BinOp(
                    left=ast.Constant(random.randint(100, 999)),
                    op=random.choice([ast.Add(), ast.Sub(), ast.Mult()]),
                    right=ast.Constant(random.randint(100, 999))
                )
            ))
        
        dead_ifs = []
        for _ in range(random.randint(0, 2)):
            dead_ifs.append(ast.If(
                test=ast.Compare(
                    left=ast.Constant(random.randint(1, 100)),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(random.randint(200, 300))]  # Luôn false
                ),
                body=[ast.Expr(value=ast.Constant(None))],
                orelse=[]
            ))
        
        insert_pos = 1 if (node.body and isinstance(node.body[0], ast.Expr) and 
                          isinstance(node.body[0].value, ast.Constant) and 
                          isinstance(node.body[0].value.value, str)) else 0
        
        node.body[insert_pos:insert_pos] = dead_vars + dead_ifs
        return node


class ImportObfuscator(ast.NodeTransformer):
    """
    obfuscate import statements
    """
    def visit_Import(self, node: ast.Import):
        for alias in node.names:
            if alias.name.startswith('Crypto'):
                return node
        
        new_body = []
        for alias in node.names:
            if alias.asname:
                new_body.append(ast.Assign(
                    targets=[ast.Name(id=alias.asname, ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='__import__', ctx=ast.Load()),
                        args=[ast.Constant(value=alias.name)],
                        keywords=[]
                    )
                ))
            else:
                name = alias.name.split('.')[0]
                new_body.append(ast.Assign(
                    targets=[ast.Name(id=name, ctx=ast.Store())],
                    value=ast.Call(
                        func=ast.Name(id='__import__', ctx=ast.Load()),
                        args=[ast.Constant(value=alias.name)],
                        keywords=[]
                    )
                ))
        return new_body if new_body else node
    
    def visit_ImportFrom(self, node: ast.ImportFrom):
        if node.module and node.module.startswith('Crypto'):
            return node
        
        if node.module is None:
            return node
        
        new_body = []
        module_var = _rand_ident("_mod_", 8)
        
        new_body.append(ast.Assign(
            targets=[ast.Name(id=module_var, ctx=ast.Store())],
            value=ast.Call(
                func=ast.Name(id='__import__', ctx=ast.Load()),
                args=[ast.Constant(value=node.module)],
                keywords=[]
            )
        ))
        
        for alias in node.names:
            target_name = alias.asname if alias.asname else alias.name
            new_body.append(ast.Assign(
                targets=[ast.Name(id=target_name, ctx=ast.Store())],
                value=ast.Call(
                    func=ast.Name(id='getattr', ctx=ast.Load()),
                    args=[
                        ast.Name(id=module_var, ctx=ast.Load()),
                        ast.Constant(value=alias.name)
                    ],
                    keywords=[]
                )
            ))
        
        return new_body if new_body else node


class StringEncryptor(ast.NodeTransformer):
    """
    mã hóa string và bytes literals (không bao gồm các thành phần f-string)
    sử dụng AES-CBC và thay thế chúng bằng _decrypt_str(b"...") hoặc
    _decrypt_bytes(b"...").
    """
    def __init__(self, key: bytes, iv: bytes):
        self.key = key
        self.iv = iv
        self.in_fstring = False

    def _encrypt(self, data: bytes) -> bytes:
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        return cipher.encrypt(pad(data, AES.block_size))

    def visit_JoinedStr(self, node: ast.JoinedStr):
        self.in_fstring = True
        self.generic_visit(node)
        self.in_fstring = False
        return node

    def visit_Constant(self, node: ast.Constant):
        if self.in_fstring:
            return node

        if isinstance(node.value, str):
            encrypted = self._encrypt(node.value.encode("utf-8"))
            return ast.Call(
                func=ast.Name(id="_decrypt_str", ctx=ast.Load()),
                args=[ast.Constant(value=encrypted)],
                keywords=[]
            )

        if isinstance(node.value, (bytes, bytearray)):
            encrypted = self._encrypt(bytes(node.value))
            return ast.Call(
                func=ast.Name(id="_decrypt_bytes", ctx=ast.Load()),
                args=[ast.Constant(value=encrypted)],
                keywords=[]
            )

        return node


class UltimateObfuscator:
    """
    bắt đầu obfuscate
    """

    def __init__(self, filename: str, encryption_level: int = 2, anti_debug: bool = True, anti_vm: bool = True, 
                 dead_code: bool = True, import_obf: bool = True):
        self.filename = filename
        self.code = self._read_file()
        self.encryption_level = encryption_level  # 1=basic, 2=standard, 3=maximum
        self.anti_debug = anti_debug  
        self.anti_vm = anti_vm  
        self.dead_code = dead_code  
        self.import_obf = import_obf  
        
        self.aes_key = os.urandom(32)  # AES-256
        self.iv = os.urandom(16)       # AES Hash

        self.k_parts = self._split_key(self.aes_key, 4 if encryption_level >= 3 else 3)
        self.iv_parts = self._split_key(self.iv, 3 if encryption_level >= 3 else 2)

    def _read_file(self) -> str:
        with open(self.filename, "r", encoding="utf-8") as f:
            return f.read()

    @staticmethod
    def _split_key(key: bytes, parts: int):
        """
        .... những người biết?
        """
        if parts < 2:
            return [key]

        length = len(key)
        rand_parts = [os.urandom(length) for _ in range(parts - 1)]

        last = bytearray(key)
        for rp in rand_parts:
            last = bytearray(a ^ b for a, b in zip(last, rp))
        rand_parts.append(bytes(last))
        return rand_parts

    def _transform_ast(self) -> bytes:
        tree = ast.parse(self.code)

        collector = VariableCollector()
        collector.visit(tree)
        assigned_vars = collector.assigned_vars - collector.global_vars
        arg_names = collector.arg_names

        transformers = []
        
        if self.import_obf:
            transformers.append(ImportObfuscator())
        
        transformers.append(ConstantObfuscator())
        
        transformers.append(VariableRenamer(assigned_vars, arg_names))
        
        if self.dead_code:
            transformers.append(DeadCodeInjector())
        
        transformers.append(ControlFlowFlattener())
        
        transformers.append(StringEncryptor(self.aes_key, self.iv))

        for tr in transformers:
            tree = tr.visit(tree)
            ast.fix_missing_locations(tree)

        code_obj = compile(tree, "<obfuscated>", "exec")
        return marshal.dumps(code_obj)

    def _build_loader(self, encrypted_data: str, payload_hash: str, recovery_key: str) -> str:
        """
        build 1 loader để chạy obfuscate
        """
        anti_debug_name = _rand_ident()
        anti_vm_name = _rand_ident()
        anti_inject_name = _rand_ident()
        main_func_name = _rand_ident()
        dec_str_name = _rand_ident()
        dec_bytes_name = _rand_ident()
        junk_func_1 = _rand_ident()
        junk_func_2 = _rand_ident()
        reconstruct_name = _rand_ident()
        key_parts_name = _rand_ident()
        iv_parts_name = _rand_ident()
        key_name = _rand_ident()
        iv_name = _rand_ident()
        decrypt_str_name = _rand_ident()
        decrypt_bytes_name = _rand_ident()
        encrypted_var_name = _rand_ident()
        blob_name = _rand_ident()
        nonce_name = _rand_ident()
        tag_name = _rand_ident()
        ciphertext_name = _rand_ident()
        cipher_name = _rand_ident()
        decrypted_data_name = _rand_ident()
        decompressed_data_name = _rand_ident()
        ns_name = _rand_ident()
        
        timestamp = datetime.now().strftime("%d/%m/%Y")

        k_parts_repr = ", ".join(repr(p) for p in self.k_parts)
        iv_parts_repr = ", ".join(repr(p) for p in self.iv_parts)

        usernames_blob = base64.b64encode(str(blacklist_usernames).encode()).decode()
        hostnames_blob = base64.b64encode(str(blacklist_hostnames).encode()).decode()
        hwids_blob = base64.b64encode(str(blacklist_hwids).encode()).decode()
        programs_blob = base64.b64encode(str(blacklist_programs).encode()).decode()
        
        anti_debug_call = f"{anti_debug_name}()" if self.anti_debug else "# Anti-debug disabled"
        vm_check_line = f"{anti_vm_name}()" if self.anti_vm else "# VM detection disabled"
        junk_calls = f"        _ = {junk_func_1}()\n        _ = {junk_func_2}(\"obf\")"
        junk_funcs_def = f"""def {junk_func_1}():
    v = 0
    for i in range(5):
        v ^= (i * 31337) << (i % 3)
    return v


def {junk_func_2}(text="junk"):
    return "-".join(reversed(list(text)))


"""

        loader = f"""# Obfuscated by FutureVisions Obfuscator
# Author: 16z aka kaefis
# GitHub: https://github.com/kaefis
# Time: {timestamp}
# Don't change ANYTHING or else code wont working

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


def {anti_debug_name}():
    try:
        if sys.gettrace():
            raise SystemExit

        try:
            import getpass
            username = getpass.getuser().lower()
            blacklist_usernames = _decode_list("{usernames_blob}")
            if username in blacklist_usernames:
                raise SystemExit
        except Exception:
            pass

        # Check hostname blacklist
        try:
            import socket
            hostname = socket.gethostname().upper()
            blacklist_hostnames = _decode_list("{hostnames_blob}")
            if hostname in blacklist_hostnames:
                raise SystemExit
        except Exception:
            pass

        # Check HWID blacklist
        try:
            import uuid
            hwid = str(uuid.getnode()).upper()
            blacklist_hwids = _decode_list("{hwids_blob}")
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
                blacklist_programs = _decode_list("{programs_blob}")
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


def {anti_vm_name}():
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
                mac_bytes.append('{{:02x}}'.format(byte_val))
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


{anti_debug_call}
{vm_check_line}


def {anti_inject_name}(data: bytes, expect_hash: str):
    import hashlib
    digest = hashlib.sha256(data).hexdigest()
    if digest != expect_hash:
        raise SystemExit("Integrity check failed")


def {reconstruct_name}(parts):
    from functools import reduce
    return reduce(lambda a, b: bytes(x ^ y for x, y in zip(a, b)), parts)


{key_parts_name} = [{k_parts_repr}]
{iv_parts_name} = [{iv_parts_repr}]

{key_name} = {reconstruct_name}({key_parts_name})
{iv_name} = {reconstruct_name}({iv_parts_name})


def {dec_str_name}(data: bytes) -> str:
    try:
        {cipher_name} = AES.new({key_name}, AES.MODE_CBC, {iv_name})
        return unpad({cipher_name}.decrypt(data), 16).decode("utf-8", errors="ignore")
    except Exception:
        return ""


def {dec_bytes_name}(data: bytes) -> bytes:
    try:
        {cipher_name} = AES.new({key_name}, AES.MODE_CBC, {iv_name})
        return unpad({cipher_name}.decrypt(data), 16)
    except Exception:
        return b""


{decrypt_str_name} = {dec_str_name}
{decrypt_bytes_name} = {dec_bytes_name}


{junk_funcs_def}

def {main_func_name}():
    try:
        {encrypted_var_name} = {encrypted_data!r}

        {blob_name} = base64.b85decode({encrypted_var_name})
        {nonce_name}, {tag_name}, {ciphertext_name} = {blob_name}[:16], {blob_name}[16:32], {blob_name}[32:]

        {cipher_name} = AES.new({key_name}, AES.MODE_GCM, nonce={nonce_name})
        {decrypted_data_name} = {cipher_name}.decrypt_and_verify({ciphertext_name}, {tag_name})
        {anti_inject_name}({decrypted_data_name}, {payload_hash!r})
        {decompressed_data_name} = zlib.decompress({decrypted_data_name})

{junk_calls}

        {ns_name} = {{
            "__name__": "__main__",
            "__builtins__": __builtins__,
            "_decrypt_str": {decrypt_str_name},
            "_decrypt_bytes": {decrypt_bytes_name},
        }}

        exec(marshal.loads({decompressed_data_name}), {ns_name})
    except Exception:
        print("Execution failed:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    {main_func_name}()
"""
        return loader

    def obfuscate(self, output_file: str = "obfuscated_" + datetime.now().strftime("%Y%m%d%H%S") + ".py", one_line: bool = False):
        try:
            transformed = self._transform_ast()
            compressed = zlib.compress(transformed, level=9)
            
            cipher = AES.new(self.aes_key, AES.MODE_GCM)
            ciphertext, tag = cipher.encrypt_and_digest(compressed)
            payload = cipher.nonce + tag + ciphertext
            
            encrypted_b85 = base64.b85encode(payload).decode("ascii")

            payload_hash = hashlib.sha256(compressed).hexdigest()
            
            recovery_data = self.aes_key + self.iv + datetime.now().isoformat().encode()
            recovery_key = hashlib.sha256(recovery_data).hexdigest()[:32]
            
            loader_src = self._build_loader(encrypted_b85, payload_hash, recovery_key)

            if one_line:
                packed_loader = zlib.compress(loader_src.encode("utf-8"), level=9)
                packed_b85 = base64.b85encode(packed_loader).decode("ascii")
                loader = f"import base64,zlib;exec(zlib.decompress(base64.b85decode({packed_b85!r})).decode())"
            else:
                loader = loader_src

            with open(output_file, "w", encoding="utf-8") as f:
                f.write(loader)

            print(fade.purpleblue(_center_text(f"[SUCCESS] Obfuscated → {output_file}")))
            print(fade.purpleblue(_center_text(f"[KEY] {recovery_key}")))
            print(fade.purpleblue(_center_text("Key được sử dụng trong trường hợp deobfuscation")))
        except Exception as e:
            raise Exception(f"Obfuscation failed: {str(e)}")

def _is_already_obfuscated(filename: str) -> bool:
    """
   kiểm tra chữ ký của future visions
    """
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            specific_signatures = [
                "FutureVisions Obfuscator",
                "Obfuscated by FutureVisions",
                "Author: 16z",
            ]
            obf_patterns = [
                "marshal.loads",
                "zlib.decompress",
                "base64.b85decode",
                "_decrypt_str",
                "_decrypt_bytes"
            ]
            
            found_specific = sum(1 for sig in specific_signatures if sig in content)
            found_patterns = sum(1 for pattern in obf_patterns if pattern in content)
            
            return found_specific >= 1 or found_patterns >= 3
    except Exception:
        return False


def _uses_terminal(filename: str) -> bool:
    """
    kiểm tra xem có dùng terminal không
    """
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
        
        try:
            tree = ast.parse(content)
        except:
            terminal_keywords = [
                r'\bprint\s*\(',
                r'\binput\s*\(',
                r'sys\.stdout',
                r'sys\.stderr',
                r'sys\.stdin',
                r'\.write\s*\(',
                r'\.read\s*\(',
            ]
            for pattern in terminal_keywords:
                if re.search(pattern, content):
                    return True
            return False
        
        class TerminalDetector(ast.NodeVisitor):
            def __init__(self):
                self.uses_terminal = False
            
            def visit_Call(self, node):
                if isinstance(node.func, ast.Name):
                    if node.func.id in ['print', 'input']:
                        self.uses_terminal = True
                elif isinstance(node.func, ast.Attribute):
                    if isinstance(node.func.value, ast.Name):
                        if node.func.value.id == 'sys' and node.func.attr in ['stdout', 'stderr', 'stdin']:
                            self.uses_terminal = True
                    if node.func.attr in ['write', 'read', 'readline', 'readlines']:
                        self.uses_terminal = True
                self.generic_visit(node)
        
        detector = TerminalDetector()
        detector.visit(tree)
        return detector.uses_terminal
    except Exception:
        # nếu có lỗi,mặc định là có dùng terminal để an toàn
        return True


def _center_text(text: str) -> str:
    width = shutil.get_terminal_size(fallback=(80, 20)).columns
    return text.center(width)

def _center_multiline(text: str) -> str:
    """căn lề"""
    width = shutil.get_terminal_size(fallback=(80, 20)).columns
    lines = text.split('\n')
    centered_lines = []
    for line in lines:
        if line.strip():
            centered_lines.append(line.center(width))
        else:
            centered_lines.append('')
    return '\n'.join(centered_lines)

# generate banner
BANNER ="""██████    ██▄▄▄█████▓█    ██ ██▀███ ▓███████▒   █▓██▓ ██████ ██▓▒█████  ███▄    █  ██████ 
▓██   ▒██  ▓██▓  ██▒ ▓▒██  ▓██▓██ ▒ ██▓█   ▓██░   █▓██▒██    ▒▓██▒██▒  ██▒██ ▀█   █▒██    ▒ 
▒████ ▓██  ▒██▒ ▓██░ ▒▓██  ▒██▓██ ░▄█ ▒███  ▓██  █▒▒██░ ▓██▄  ▒██▒██░  ██▓██  ▀█ ██░ ▓██▄   
░▓█▒  ▓▓█  ░██░ ▓██▓ ░▓▓█  ░██▒██▀▀█▄ ▒▓█  ▄ ▒██ █░░██░ ▒   ██░██▒██   ██▓██▒  ▐▌██▒ ▒   ██▒
░▒█░  ▒▒█████▓  ▒██▒ ░▒▒█████▓░██▓ ▒██░▒████▒ ▒▀█░ ░██▒██████▒░██░ ████▓▒▒██░   ▓██▒██████▒▒
 ▒ ░  ░▒▓▒ ▒ ▒  ▒ ░░  ░▒▓▒ ▒ ▒░ ▒▓ ░▒▓░░ ▒░ ░ ░ ▐░ ░▓ ▒ ▒▓▒ ▒ ░▓ ░ ▒░▒░▒░░ ▒░   ▒ ▒▒ ▒▓▒ ▒ ░
 ░    ░░▒░ ░ ░    ░   ░░▒░ ░ ░  ░▒ ░ ▒░░ ░  ░ ░ ░░  ▒ ░ ░▒  ░ ░▒ ░ ░ ▒ ▒░░ ░░   ░ ▒░ ░▒  ░ ░
 ░ ░   ░░░ ░ ░  ░      ░░░ ░ ░  ░░   ░   ░      ░░  ▒ ░  ░  ░  ▒ ░ ░ ░ ▒    ░   ░ ░░  ░  ░  
         ░               ░       ░       ░  ░    ░  ░       ░  ░     ░ ░          ░      ░   
"""

def show_header():
    centered_banner = _center_multiline(BANNER)
    faded_banner = fade.purpleblue(centered_banner)
    print(faded_banner)
    print()
    print(fade.purpleblue(_center_text("GitHub: https://github.com/kaefis")))
    print(fade.purpleblue(_center_text("Author: 16z")))


def main():
    while True:
        try:
            os.system("cls" if os.name == "nt" else "clear")
            show_header()

            def _prompt_tab(prompt_text: str) -> str:
                prompt_text = prompt_text.rstrip("\n")
                return input("\t" + prompt_text)
            
            filename = _prompt_tab(fade.purpleblue("[+] Path: ")).strip()
            if not filename:
                print(fade.purpleblue(_center_text("Không hợp lệ")))
                time.sleep(2)
                continue
            if not os.path.isfile(filename):
                print(fade.purpleblue(_center_text(f"Không tìm thấy file: {filename}")))
                time.sleep(2)
                continue
            
            if _is_already_obfuscated(filename):
                print(fade.purpleblue(_center_text("[!] File này đã từng được obfuscate bởi FutureVisions!")))
                print(fade.purpleblue(_center_text("[!] Không nên obfuscate lại file đã obfuscate.")))
                continue_choice = _prompt_tab(fade.purpleblue("[?] Bạn có muốn tiếp tục? (y/n): ")).strip().lower()
                if continue_choice != "y":
                    time.sleep(2)
                    os.system("cls" if os.name == "nt" else "clear")
                    continue

            output_prompt = fade.purpleblue("[+] Tên file xuất(có thể bỏ qua): ")
            output_file = _prompt_tab(output_prompt).strip() or "obfuscated_" + datetime.now().strftime("%Y%m%d%H%M") + ".py"

            compile_exe_prompt = fade.purpleblue("[~][WIP] Compile thành exe? (y/n): ")
            compile_exe_choice = _prompt_tab(compile_exe_prompt).strip().lower().startswith("y")
            
            one_line_choice = False
            if not compile_exe_choice:
                one_line_prompt = fade.purpleblue("[~] 1-line obfuscate?: ")
                one_line_choice = _prompt_tab(one_line_prompt).strip().lower().startswith("y")

            anti_debug_prompt = fade.purpleblue("[~] Anti-Debug? (y/n): ")
            anti_debug_choice = _prompt_tab(anti_debug_prompt).strip().lower()
            anti_debug_enabled = anti_debug_choice != "n" if anti_debug_choice else True
            
            anti_vm_prompt = fade.purpleblue("[~] Anti-VM? (y/n): ")
            anti_vm_choice = _prompt_tab(anti_vm_prompt).strip().lower()
            anti_vm_enabled = anti_vm_choice != "n" if anti_vm_choice else True
            
            dead_code_prompt = fade.purpleblue("[~] Dead Code Injection? (y/n): ")
            dead_code_choice = _prompt_tab(dead_code_prompt).strip().lower()
            dead_code_enabled = dead_code_choice != "n" if dead_code_choice else True
            
            import_obf_prompt = fade.purpleblue("[~] Import Obfuscation? (y/n): ")
            import_obf_choice = _prompt_tab(import_obf_prompt).strip().lower()
            import_obf_enabled = import_obf_choice != "n" if import_obf_choice else True
            
            try:
                print(fade.purpleblue(_center_text(f"[*] Đang obfuscate file: {filename}")))
                obf = UltimateObfuscator(
                    filename, 
                    encryption_level=3, 
                    anti_debug=anti_debug_enabled,
                    anti_vm=anti_vm_enabled,
                    dead_code=dead_code_enabled,
                    import_obf=import_obf_enabled
                )
                obf.obfuscate(output_file=output_file, one_line=one_line_choice)
                print(fade.purpleblue(_center_text(f"[+] Obfuscate thành công!")))
            except Exception as e:
                print(fade.purpleblue(_center_text(f"[!] Lỗi khi obfuscate: {str(e)}")))
                time.sleep(2)
                continue

            if compile_exe_choice:  

                try:
                    print(fade.purpleblue(_center_text("[*] Đang compile thành exe")))
                    import subprocess
                    exe_output = os.path.splitext(output_file)[0] + ".exe"
                    
                    # kiểm tra xem code có dùng terminal không
                    uses_terminal = _uses_terminal(filename)
                    
                    pyinstaller_cmd = [
                    sys.executable, "-m", "PyInstaller",
                    "--onefile",
                    "--name", os.path.splitext(exe_output)[0],
                    ]
                    
                    # nếu không dùng terminal thì thêm --noconsole
                    if not uses_terminal:
                        pyinstaller_cmd.append("--noconsole")
                    else:
                        pass

                    pyinstaller_cmd.append(output_file)

                    try:
                        import PyInstaller
                    except ImportError:
                        print(fade.purpleblue(_center_text("[!] PyInstaller chưa được cài đặt,đang cài đặt...")))
                    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller", "-q"])
                    pyinstaller_cmd = [c for c in pyinstaller_cmd if c]
                    
                    result = subprocess.run(pyinstaller_cmd, capture_output=True, text=True)
                    
                    if result.returncode == 0:
                        dist_exe = os.path.join("dist", os.path.basename(exe_output))
                        build_exe = os.path.join("build", os.path.basename(exe_output))

                        moved = False
                        if os.path.exists(dist_exe):
                            shutil.move(dist_exe, exe_output)
                            moved = True
                        elif os.path.exists(build_exe):
                            shutil.move(build_exe, exe_output)
                            moved = True

                        if os.path.exists("build"):
                            shutil.rmtree("build")
                        if os.path.exists("dist"):
                            shutil.rmtree("dist")
                        spec_file = os.path.splitext(exe_output)[0] + ".spec"
                        if os.path.exists(spec_file):
                            os.remove(spec_file)

                        try:
                            if os.path.exists(output_file):
                                os.remove(output_file)
                        except Exception:
                            pass

                        if moved:
                            print(fade.purpleblue(_center_text(f"[SUCCESS] Đã compile thành exe → {exe_output}")))
                        else:
                            print(fade.purpleblue(_center_text("[!] Không tìm thấy file exe đã compile")))
                    else:
                        print(fade.purpleblue(_center_text(f"[!] Lỗi khi compile: {result.stderr}")))
                except Exception as e:
                    print(fade.purpleblue(_center_text(f"[!] Lỗi khi compile exe: {str(e)}")))
                    time.sleep(3)

            print(fade.purpleblue(_center_text("[*] Done..")))
            time.sleep(3)

        except KeyboardInterrupt:
            print()
            print(fade.purpleblue(_center_text("[!] Ctrl-C detected")))
            sys.exit(0)
        except Exception as e:
            print(fade.purpleblue(_center_text(f"[!] Lỗi: {str(e)}")))
            time.sleep(4)
            continue


if __name__ == "__main__":
    main()
